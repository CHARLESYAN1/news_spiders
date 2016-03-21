from datetime import date, timedelta

from .. import app
from ..transfer.base import Base
from news_spiders.utils import Mongodb
from news_spiders.utils.utils import populate_md5, recognise_chz


def get_md5_from_mongo(self):
    required_scrapy = []
    required_filtering = []

    collection = Mongodb(
        host=self.config['AMAZON_BJ_MONGO_HOST'],
        port=self.config['AMAZON_BJ_MONGO_PORT'],
        database=self.config['AMAZON_BJ_MONGO_DB'],
        collection=self.config['AMAZON_BJ_MONGO_TABLE']
    )

    query_scrapy = {
        'dt': {
            '$lte': str(date.today()).replace('-', '') + '000000',
            '$gte': str(date.today() - timedelta(days=2)).replace('-', '') + '235959'
        }
    }

    query_filtering = {
        'dt': {
            '$lte': str(date.today() - timedelta(days=365)).replace('-', '') + '000000',
            '$gte': str(date.today() - timedelta(days=425)).replace('-', '') + '235959'
        }
    }

    for _docs in collection.query(query_scrapy, {'url': 1, 't': 1}):
        required_scrapy.append(populate_md5(_docs['url']))
        required_scrapy.append(populate_md5(recognise_chz(_docs['t'])))

    for _docs in collection.query(query_filtering, {'url': 1, 't': 1}):
        required_filtering.append(populate_md5(_docs['url']))
        required_filtering.append(populate_md5(recognise_chz(_docs['t'])))

    return required_scrapy, required_filtering


@app.scheduled_job(trigger='cron', hour='0', minute='0', second='30')
def clean_redis():
    """
    """
    self = Base()
    scrapy_key = self.config['SCRAPY_FILTER_KEY']
    filtering_key = self.config['REDIS_FILTER_KEY']
    required_scrapy, required_filtering = get_md5_from_mongo(self)

    # first remove scrapy_key, then add this key
    self.redis.rem(scrapy_key)
    self.redis.set(scrapy_key, *required_scrapy)

    # remove value to filtering_key
    self.redis.rem(filtering_key, *required_filtering)







