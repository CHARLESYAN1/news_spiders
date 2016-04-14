# -*- coding: utf-8 -*-

# Scrapy settings for news_spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
from .news_settings import REDIS_HOST, SCRAPY_PROXY_IP_KEY, REDIS_FILTER_KEY

BOT_NAME = 'news_spiders'

SPIDER_MODULES = ['news_spiders.spiders']
NEWSPIDER_MODULE = 'news_spiders.spiders'

CONFIG_KEY = 'conf_key'

DOWNLOAD_HANDLERS = {'s3': None, }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'news_spiders (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.8
DOWNLOAD_TIMEOUT = 15
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # 'news_spiders.middlewares.MyCustomSpiderMiddleware': 543,
    # 'news_spiders.contrib.middlewares.spidermiddleware.MewsSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'news_spiders.middlewares.MyCustomDownloaderMiddleware': 543,
    'news_spiders.middlewares.downloader.httpproxy.NewsHttpProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,

    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'news_spiders.middlewares.downloader.useragent.NewsUserAgentMiddleware': 400,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'news_spiders.pipelines.SomePipeline': 300,
    'news_spiders.pipelines.pipelines.NewsSpidersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

# Scrapy dupefilter class
DUPEFILTER_KEY = REDIS_FILTER_KEY
# DUPEFILTER_CLASS = 'news_spiders.schema.dupefilter.RFPDupeFilter'

# Scheduler Queue class and key
SCHEDULER_QUEUE_KEY = 'scheduler_queue:requests'
SCHEDULER_QUEUE_CLASS = 'news_spiders.schema.queue.PriorityQueue'

# Custom Scheduler class
SCHEDULER = 'news_spiders.schema.scheduler.Scheduler'


# ################### Redis Relative Config ######################
REDIS_HOST = REDIS_HOST
SCRAPY_PROXY_IP_KEY = SCRAPY_PROXY_IP_KEY
# ################### Redis Relative Config ######################
