# coding=utf-8
# author: shuqing.zhou

import re
import os
import time
import random
import os.path
from multiprocessing.dummy import Pool as ThreadPool

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout, ConnectTimeout, ConnectionError

from config import *
from news_spiders.conf import news_config


class HttpProxy(object):
    def __init__(self):
        self._temp = list()
        self.filename = news_config.settings['SCRAPY_PROXY_IP']

        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename))

    def run(self):
        _slice = 50
        proxies = []

        for item in PROXY_SITES:
            header = {"User-Agent": random.choice(UA)}

            try:
                if item['type'] == 're':
                    r = requests.get(item["site"], headers=header, timeout=FETCH_TIMEOUT)
                    temps = re.findall(item["re"], r.content)
                    self._temp.extend(temps)
                elif item['type'] == 'bs4':
                    for i in xrange(1, item["page"] + 1):
                        url = item["site"] % i
                        r = requests.get(url, timeout=FETCH_TIMEOUT, headers=header)
                        soup = BeautifulSoup(r.content, "lxml")

                        for detail in soup.select(item["select"]["base"]):
                            ip = detail.select("td")[item["select"]["ip"]].text
                            port = detail.select("td")[item["select"]["port"]].text
                            self._temp.append(ip.replace(" ", "") + ":" + port)
            except (ReadTimeout, ConnectTimeout, ConnectionError):
                pass

        length = len(self._temp) / 50 + 1

        pool = ThreadPool(12)
        proxies.extend(pool.map(self.test, [self._temp[i * _slice: (i + 1) * _slice] for i in range(length)]))
        pool.close()
        pool.join()

        with open(self.filename, 'w') as fp:
            fp.writelines([_proxy + '\n' for proxys in proxies for _proxy in proxys if _proxy])

    def check(self, proxy_list):
        pool = ThreadPool(12)
        pool.map(self.test, [proxy for proxy in proxy_list])
        pool.close()
        pool.join()

    @staticmethod
    def test(_proxy):

        proxies = {"http": "http://" + _proxy}
        try:
            r = requests.get(TEST_URL, proxies=proxies, timeout=3)
            status_code, content = r.status_code, r.content

            if status_code == 200 and re.compile(r'%s' % MARK, re.S).search(content):
                return _proxy
            print 'ok'
        except (ReadTimeout, ConnectTimeout, ConnectionError):
            pass
