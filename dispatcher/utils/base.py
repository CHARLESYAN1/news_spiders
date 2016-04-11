from datetime import date

from .csfpickle import CsfPickle as _Cpk
from news_spiders.conf import news_config
from news_spiders.contrib import RedisBase
from news_spiders.contrib import SmoothTransfer
from news_spiders.contrib import PickleToQueue, UnpickleToFile


class Base(object):
    def __init__(self):
        self.cached = _Cpk().load()
        self.config = news_config.settings

    @property
    def redis(self):
        return RedisBase().redis

    @property
    def smooth(self):
        return SmoothTransfer()

    @property
    def ptq(self):
        return PickleToQueue()

    @property
    def uptf(self):
        return UnpickleToFile()

    @property
    def is_migrate(self):
        return self.config['IS_MIGRATE']

    @property
    def hot_news_path(self):
        return self.config['HOT_DES_NEWS_PATH'] + str(date.today()).replace('-', '') + '/'

    @property
    def full_news_path(self):
        return self.config['NEWS_DIR_PATH'] + str(date.today()).replace('-', '') + '/'

    @property
    def mongo_args(self):
        host = self.config['AMAZON_BJ_MONGO_HOST']
        port = self.config['AMAZON_BJ_MONGO_PORT']
        db = self.config['AMAZON_BJ_MONGO_DB']
        table = self.config['AMAZON_BJ_MONGO_TABLE']
        return host, port, db, table

    def is_filtering(self, filename):
        """
        whether url or title include redis or not
        :param filename:
        """
        if filename not in self.cached:
            self.cached.add(filename)
            return True
        return False


