import random

from ...conf import news_config


class NewsHttpProxyMiddleware(object):
    def __init__(self):
        self._proxy_filename = news_config.settings.get('SCRAPY_PROXY_IP', '')

        try:
            with open(self._proxy_filename) as fp:
                self.http_proxy = [line.strip() for line in fp if line.strip()]
        except IOError:
            self.http_proxy = []

    def process_request(self, request, spider):
        if self.http_proxy:
            request.meta['proxy'] = random.choice(self.http_proxy)
