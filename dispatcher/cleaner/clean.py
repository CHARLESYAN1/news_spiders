from datetime import date, timedelta

from .. import app, logger
from ..utils import JobBase
from news_spiders.utils import Mongodb
from news_spiders.exceptions import get_exce_info
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


@app.scheduled_job(trigger='cron', hour='0', minute='0', second='30', misfire_grace_time=20)
def clean_redis():
    """ cron clean redis data """
    self = JobBase()

    if not self.is_migrate:
        return

    try:
        filtering_key = self.config['REDIS_FILTER_KEY']
        required_filtering = get_md5_from_mongo(self)
        print filtering_key, len(required_filtering)

        # Clean data from `REDIS_FILTER_KEY`
        self.redis.srem(filtering_key, *required_filtering)
    except Exception:
        logger.info(logger.exec_msg.format(msg='Clean redis data error', exec_info=get_exce_info()))







