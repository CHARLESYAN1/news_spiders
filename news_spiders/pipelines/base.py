from datetime import date, datetime
from pymongo.errors import TimeoutError, DuplicateKeyError
from pymongo.errors import ExceededMaxWaiters, AutoReconnect

from ..conf import news_config
from ..contrib import RedisBase
from ..utils import KwFilter as _KwF
from ..utils import Mongodb as _Mongo
from news_spiders.contrib import Bucket as _Bucket


class Base(object):
    required_fields = ['url', 'date', 'author',  'source', 'title', 'content', 'ratio', 'crt']

    def __init__(self):
        self._settings = news_config.settings

        self.kwf_cls = _KwF
        self.kwf_cls.redis = RedisBase().redis
        self.kwf_cls.key = self._settings['REDIS_FILTER_KEY']

        self.mongo = _Mongo(
            host=self._settings['AMAZON_BJ_MONGO_HOST'],
            port=self._settings['AMAZON_BJ_MONGO_PORT'],
            database=self._settings['AMAZON_BJ_MONGO_DB'],
            collection=self._settings['AMAZON_BJ_MONGO_CRAWLER']
        )

    @property
    def is_migrate(self):
        return self._settings['IS_MIGRATE']

    @staticmethod
    def segment(site_name):
        _segment = site_name.split('_')[0]

        if _segment == 'hot':
            return True
        elif _segment == 'gp':
            return None
        else:
            return False

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
            if self.is_migrate is True:
                data['d'] = data['dt'][:8]
                self.mongo.insert(data)
        except (TimeoutError, DuplicateKeyError, ExceededMaxWaiters, AutoReconnect) as e:
            pass

    @property
    def bucket(self):
        return _Bucket()

    @staticmethod
    def s3_key(prefix):
        """
        :param prefix: absolute local filename path
        :return:  bucket key
        """
        return prefix[1:] if prefix.startswith('/') else prefix

    def send_s3(self, local, remote):
        """
        Send yield news file to AWS s3

        :param local: absolute local filename path
        :param remote: absolute remote s3 filename path
        """
        if self.is_migrate:
            s3_key = self.s3_key(local)
            self.bucket.put(s3_key, remote)
