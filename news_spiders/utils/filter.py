import difflib

from ..conf import news_config
from ..utils import populate_md5, recognise_chz


class KwFilter(object):
    def __init__(self, is_hot, title, url):
        self.settings = news_config.settings
        self._is_hot = is_hot
        self._url = url
        self._title = title

    @staticmethod
    def string_diff(a, b):
        diff = difflib.SequenceMatcher(None, a, b)
        if int(diff.ratio() * 1000) >= 990:
            return True
        return False

    @property
    def existed_redis(self):
        t_md5 = populate_md5(recognise_chz(self._title))
        redis = getattr(self.__class__, 'redis', None)
        filter_key = getattr(self.__class__, 'key', None)

        if redis and filter_key:
            return not redis.sadd(filter_key, t_md5)

    def filter_with_kw(self, origin, is_hot):
        """
        :param origin: string, filter by keywords
        :param is_hot: bool, is True, filter hot keywords, else full keywords
        :return: 0 title isn't filter, 1 is need filter
        """
        origin = origin.strip()
        keywords = self.settings['HOT_KEYS_FILTER'] if is_hot else self.settings['TITLE_KEYS_FILTER']

        for key, values in keywords.iteritems():
            for tit in values:
                if "start" == key and self.string_diff(tit, origin[:len(tit)]):
                    return True
                elif "end" == key and self.string_diff(tit, origin[len(origin) - len(tit):]):
                    return True
                elif "in" == key and tit in origin:
                    return True
                elif "start_regex" == key and tit.search(origin):
                    return True
        return False

    @property
    def ratio(self):
        if self.existed_redis:
            return 0

        if self.filter_with_kw(self._title, self._is_hot):
            return 2
        return 1


class BloomFilter(object):
    pass







