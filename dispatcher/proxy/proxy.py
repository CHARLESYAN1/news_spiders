from . import HttpProxy
from .. import logger
from ..utils import JobBase

from news_spiders.conf import news_config
from news_spiders.exceptions import get_exce_info


# @app.scheduled_job(trigger='interval', minutes=5, misfire_grace_time=20)
def crawl_proxy_ip():
    try:
        jb = JobBase()
        if not jb.is_migrate:
            return

        total_proxy = HttpProxy().run()

        redis = jb.redis
        scrapy_proxy_ip_key = news_config.settings['SCRAPY_PROXY_IP_KEY']

        if total_proxy:
            redis.delete(scrapy_proxy_ip_key)
            redis.rpush(scrapy_proxy_ip_key, *total_proxy)
    except Exception:
        logger.info(logger.exec_msg.format(msg='Crawl proxy ip error', exec_info=get_exce_info()))
