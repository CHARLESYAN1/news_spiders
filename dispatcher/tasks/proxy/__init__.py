# coding=utf-8
# author: shuqing.zhou

import re
import os
import time
import random
import os.path
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import requests
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
                r = requests.get(item["site"], headers=header, timeout=FETCH_TIMEOUT)
                temps = re.findall(item["re"], r.content)
                self._temp.extend(temps)
            except (ReadTimeout, ConnectTimeout, ConnectionError):
                pass

        print len(self._temp)
        div, mod = divmod(len(self._temp), _slice)
        count = div + (mod and 1)

        pool = ThreadPool(12)

        dispatch_ip = [self._temp[i * _slice: (i + 1) * _slice] for i in range(count)]
        proxies.extend(pool.map(self.test, dispatch_ip))
        pool.close()
        pool.join()

        print proxies

        with open(self.filename, 'w') as fp:
            fp.writelines([_proxy + '\n' for proxys in proxies for _proxy in proxys if _proxy])

    @staticmethod
    def test(proxys):

        def inner_test(_proxy):
            proxies = {"http": "http://" + _proxy}
            try:
                r = requests.get(TEST_URL, proxies=proxies, timeout=3)
                status_code, content = r.status_code, r.content

                if status_code == 200 and re.compile(r'%s' % MARK, re.S).search(content):
                    return _proxy
                print 'ok'
            except (ReadTimeout, ConnectTimeout, ConnectionError):
                pass

        pool = ThreadPool(12)
        res = pool.map(inner_test, proxys)
        pool.close()
        pool.join()
        return res

st = time.time()
HttpProxy().run()
print time.time() - st

# print requests.get('http://proxy.mimvp.com/free.php?proxy=in_tp&sort=&pageindex=1').content