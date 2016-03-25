# coding=utf-8
# author: shuqing.zhou

import re
import random
from multiprocessing.dummy import Pool as ThreadPool

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout, ConnectTimeout, ConnectionError, ChunkedEncodingError

from config import *


class HttpProxy(object):
    @staticmethod
    def threads(func, iterable):
        pool = ThreadPool(12)
        rest = pool.map(func, iterable)
        pool.close()
        pool.join()

        return rest

    @staticmethod
    def get_data(kwargs):
        timeout = FETCH_TIMEOUT
        headers = {"User-Agent": random.choice(UA)}

        if kwargs['type'] == 're':
            regex = kwargs['re']
            r = requests.get(kwargs['site'], headers=headers, timeout=timeout)
            return re.findall(regex, r.content)

        if kwargs['type'] == 'bs4':
            bs4_ips = []

            for i in range(1, kwargs['page'] + 1):
                r = requests.get(kwargs['site'] % i, timeout=timeout, headers=headers)
                soup = BeautifulSoup(r.content, "lxml")

                for detail in soup.select(kwargs['select']['base']):
                    ip = detail.select("td")[kwargs['select']['ip']].text
                    port = detail.select("td")[kwargs['select']['port']].text
                    bs4_ips.append(ip.replace(" ", "") + ":" + port)
            return bs4_ips
        return []

    def run(self):
        _slice = 50
        before_ips = []

        try:
            overall_ips = self.threads(self.get_data, [item for item in PROXY_SITES])

            for each_ips in overall_ips:
                before_ips.extend(each_ips)
        except (ReadTimeout, ConnectTimeout, ConnectionError, ChunkedEncodingError):
            pass

        length = len(before_ips) / _slice + 1

        after_ips = self.threads(self.check, [before_ips[i * _slice: (i + 1) * _slice] for i in range(length)])
        return [_proxy for _proxy_list in after_ips for _proxy in _proxy_list if _proxy]

    def check(self, proxy_list):
        return self.threads(self.test, proxy_list)

    @staticmethod
    def test(_proxy):

        proxies = {"http": "http://" + _proxy}
        try:
            r = requests.get(TEST_URL, proxies=proxies, timeout=2)
            status_code, content = r.status_code, r.content

            if status_code == 200 and re.compile(r'%s' % MARK, re.S).search(content):
                return _proxy
        except (ReadTimeout, ConnectTimeout, ConnectionError, ChunkedEncodingError):
            pass
