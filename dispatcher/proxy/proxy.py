import os.path

from . import HttpProxy
from .. import app, logger
from news_spiders.conf import news_config
from news_spiders.contrib import RedisBase


@app.scheduled_job(trigger='interval', minutes=5)
def crawl_proxy_ip():
    try:
        total_proxy = HttpProxy().run()

        redis = RedisBase().redis
        scrapy_proxy_ip_key = news_config.settings['SCRAPY_PROXY_IP_KEY']

        if total_proxy:
            redis.delete(scrapy_proxy_ip_key)
            redis.rpush(scrapy_proxy_ip_key, *total_proxy)
    except Exception as e:
        logger.info('Crawl proxy ip error: type <{}>, msg <{}>, file <{}>'.format(
            e.__class__, e, os.path.abspath(__file__)))
