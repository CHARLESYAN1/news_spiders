# -*- coding: utf-8 -*-
import difflib

from ..conf import news_config
from ..urlsresolver import BaseURi
from ..utils import populate_md5, recognise_chz


class KwFilter(object):
    def __init__(self, is_hot, title, url):
        self.settings = news_config.settings
        self._is_hot = is_hot
        self._url = url
        self._title = title
        self._hostname = BaseURi.hostname(self._url)

    @staticmethod
    def string_diff(a, b):
        diff = difflib.SequenceMatcher(None, a, b)
        if int(diff.ratio() * 1000) >= 990:
            return True
        return False

    @property
    def existed_redis(self):
        if 'weixin' in self._hostname and 'qq' in self._hostname:
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

    def discard_title(self):
        """ 主要去除微信文章里的部分文章 """
        discard_title_kw = self.settings.get('DISCARD_TITLE_ARTICLE', [])

        if 'weixin' in self._hostname and 'qq' in self._hostname:
            for word in discard_title_kw:
                if word in self._title:
                    return True
        return False

    @property
    def ratio(self):
        """ 过滤顺序不要改变 """
        # If title of article have kw, that article need to discard
        if self.discard_title():
            return 0

        # Only deal with weixin article according to url
        if self.existed_redis:
            return 0

        if self.filter_with_kw(self._title, self._is_hot):
            return 2
        return 1


class BloomFilter(object):
    pass







