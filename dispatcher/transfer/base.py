from datetime import date

from news_spiders.conf import news_config
from news_spiders.contrib import RedisCached
from news_spiders.contrib import GoosyTransfer, Bucket
from news_spiders.contrib import PickleToQueue, UnpickleToFile
from news_spiders.utils.utils import populate_md5, recognise_chz


class Base(object):
    def __init__(self):
        self.cached = set()
        self.config = news_config.settings

    @property
    def goosy(self):
        return GoosyTransfer()

    @property
    def bucket(self):
        return Bucket()

    @property
    def ptq(self):
        return PickleToQueue()

    @property
    def uptf(self):
        return UnpickleToFile()

    @staticmethod
    def s3_key(prefix, filename):
        s3_prefix = prefix[1:] if prefix.startswith('/') else prefix
        return s3_prefix + filename

    @property
    def is_migrate(self):
        return self.config['IS_MIGRATE']

    @property
    def hot_news_path(self):
        return self.config['HOT_DES_NEWS_PATH'] + str(date.today()).replace('-', '') + '/'

    @property
    def full_news_path(self):
        return self.config['NEWS_DIR_PATH'] + str(date.today()).replace('-', '') + '/'

    def filter_files(self, filename):
        """
        whether url or title include redis or not
        :param filename:
        """
        with open(filename) as fp:
            lines = fp.readlines()
            url = lines[0].strip()
            title = lines[4].strip()

        is_filtering = False
        url_md5 = populate_md5(url)
        tit_md5 = populate_md5(recognise_chz(title))

        if url_md5 not in self.cached:
            self.cached.add(tit_md5)
            is_filtering = True

        if tit_md5 not in self.cached:
            self.cached.add(tit_md5)
            is_filtering = True

        return is_filtering


