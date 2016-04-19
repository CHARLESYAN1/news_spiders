import os
import re
import linecache
from os.path import join
from datetime import date
from collections import defaultdict

from tld import get_tld
from ..utils import JobBase
from news_spiders.utils import Mongodb


class StatisticsBase(object):
    def __init__(self):
        self.topnews = self._parse(self._hot_dataset())
        self.hotnews = self._parse(self._top_dataset())

    def _top_dataset(self):
        raise NotImplemented

    def _hot_dataset(self):
        raise NotImplemented

    @staticmethod
    def _parse(dataset):
        result = defaultdict(lambda: defaultdict(int))

        for uri, cat in dataset:
            domain = get_tld(uri, as_object=True).domain
            result[domain][cat] += 1
            result[domain]['count'] += 1
        return result

    def show(self):
        def inner(dataset):
            for site, vaules in dataset.iteritems():
                print('top news show:')
                for _key, _count in vaules.iteritems():
                    print('\t{}->{}: {}'.format(site, _key, _count))

        inner(self.topnews)
        print('top site len: {}'.format(len(self.topnews)))
        inner(self.hotnews)
        print('all site len: {}'.format(len(self.hotnews)))


class StatisticsBefore(StatisticsBase):
    @staticmethod
    def _get_data_from_files(path):
        data = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                abs_filename = join(root, filename)
                url = linecache.getline(abs_filename, 1).strip()
                cat = linecache.getline(abs_filename, 4).strip()
                data.append((url, cat))
        return data

    def _top_dataset(self):
        hot_path = JobBase().hot_news_path
        return self._get_data_from_files(hot_path)

    def _hot_dataset(self):
        full_path = JobBase().full_news_path
        return self._get_data_from_files(full_path)


class StatisticsAfter(StatisticsBase):
    def __init__(self, query_date=None):
        if query_date is None:
            self.query_date = str(date.today()).replace('-', '')
        else:
            if not isinstance(query_date, basestring) or len(query_date) != 8:
                raise ValueError("<query_date> must string and length is 8")
            self.query_date = query_date

        super(self.__class__, self).__init__()

    def _get_data_from_mongo(self, mongo_args):
        mongo = Mongodb(*mongo_args)
        fields = {'url': 1, 'cat': 1}
        query = {'dt': re.compile(r'%s' % self.query_date)}

        return [(docs['url'], docs['cat']) for docs in mongo.query(query, fields)]

    def _top_dataset(self):
        mongo_args = JobBase().mongo_args[:-1]
        hot_mongo_args = mongo_args + ('hotnews_analyse', )
        return self._get_data_from_mongo(*hot_mongo_args)

    def _hot_dataset(self):
        mongo_args = JobBase().mongo_args[:-1]
        hot_mongo_args = mongo_args + ('hotnews_analyse',)
        return self._get_data_from_mongo(*hot_mongo_args)

