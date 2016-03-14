from datetime import date

from ..contrib import RedisCached
from ..contrib import redis_cached
from ..conf import news_config
from ..utils import KwFilter as _KwF


class Base(object):
    def __init__(self):
        _KwF.redis = self.redis
        _KwF.cached = redis_cached
        self.kwf_cls = _KwF
        self._settings = news_config.settings

    @property
    def redis(self):
        return RedisCached()

    @staticmethod
    def segment(site_name):
        return site_name.split('_')[0]

    def store_path(self, is_hot):
        ymd = str(date.today()).split('-')

        if not is_hot:
            path = self._settings['NEWS_DIR_PATH'] + ''.join(ymd) + '/'
        else:
            path = self._settings['HOT_ORI_NEWS_PATH'] + ''.join(ymd) + '/h_'
        return path







