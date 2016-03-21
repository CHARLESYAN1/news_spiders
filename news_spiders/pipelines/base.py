from datetime import date, datetime
from pymongo.errors import TimeoutError, DuplicateKeyError
from pymongo.errors import ExceededMaxWaiters, AutoReconnect

from ..conf import news_config
from ..utils import KwFilter as _KwF
from ..utils import Mongodb as _Mongo


class Base(object):
    required_fields = ['url', 'dt', 'auth',  'cat', 'title', 'text', 'ratio', 'crt']

    def __init__(self):
        self.kwf_cls = _KwF
        self._settings = news_config.settings
        self.mongo = _Mongo(
            host=self._settings['AMAZON_BJ_MONGO_HOST'],
            port=self._settings['AMAZON_BJ_MONGO_PORT'],
            database=self._settings['AMAZON_BJ_MONGO_DB'],
            collection=self._settings['AMAZON_BJ_MONGO_TABLE']
        )

    @staticmethod
    def segment(site_name):
        return site_name.split('_')[0]

    def store_path(self, is_hot):
        ymd = str(date.today()).split('-')

        if not is_hot:
            path = self._settings['NEWS_DIR_PATH'] + ''.join(ymd) + '/'
        else:
            path = self._settings['HOT_DES_NEWS_PATH'] + ''.join(ymd) + '/h_'
        return path

    @property
    def crt(self):
        return str(datetime.now()).replace('-', '').replace(' ', '').replace(':', '')[:14]

    def insert2mongo(self, data):
        try:
            self.mongo.insert(data)
        except (TimeoutError, DuplicateKeyError, ExceededMaxWaiters, AutoReconnect) as e:
            pass
