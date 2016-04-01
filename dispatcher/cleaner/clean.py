from os.path import abspath as _abs
from datetime import date, timedelta

from .. import app, logger
from ..utils import JobBase
from news_spiders.utils import Mongodb
from news_spiders.utils import populate_md5, recognise_chz


def get_md5_from_mongo(self):
    required_filtering = []

    collection = Mongodb(*self.mongo_args)

    query_filtering = {
        'dt': {
            '$lte': str(date.today() - timedelta(days=365)).replace('-', '') + '000000',
            '$gte': str(date.today() - timedelta(days=425)).replace('-', '') + '235959'
        }
    }

    for _docs in collection.query(query_filtering, {'url': 1, 't': 1}):
        required_filtering.append(populate_md5(_docs['url']))
        required_filtering.append(populate_md5(recognise_chz(_docs['t'])))

    collection.disconnect()
    return required_filtering


@app.scheduled_job(trigger='cron', hour='0', minute='0', second='30')
def clean_redis():
    """ cron clean redis data """
    self = JobBase()

    if self.is_migrate is not True:
        return

    try:
        filtering_key = self.config['REDIS_FILTER_KEY']
        required_scrapy, required_filtering = get_md5_from_mongo(self)

        # Clean data from `REDIS_FILTER_KEY`
        self.redis.rem(filtering_key, *required_filtering)
    except Exception as e:
        info = (e.__class__, e, _abs(__file__))
        logger.info('Clean redis data error: type <{}>, msg <{}>, file <{}>'.format(*info))







