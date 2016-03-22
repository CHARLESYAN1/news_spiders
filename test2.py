from news_spiders.utils.logger import Logger
log = Logger('error')
log.info('cao cao')


from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.downloadermiddlewares.stats import DownloaderStats
