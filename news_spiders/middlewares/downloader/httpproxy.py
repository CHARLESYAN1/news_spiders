from ...conf import news_config


class NewsHttpProxyMiddleware(object):
    def __init__(self):
        self._proxy_ip_redis_key = news_config.settings['']

    def process_request(self, request, spider):
        pass
