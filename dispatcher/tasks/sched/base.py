# -*- coding: utf-8 -*-
import os
import os.path
import time
from collections import defaultdict
from datetime import date, timedelta

import tld
from scrapyd_api import ScrapydAPI

from dispatcher import app
from news_spiders.conf import news_config
from . import conf


class Intervals(object):
    """
    Three time interval:
    (1): default 06:00-10:00 for 5 minutes interval, at least 2 minutes
    (2): default 10:00-20:00 for 8 minuets interval, at least 3 minutes
    (3): default 20:00-23:59 and 00:00-06:00 for 10 minutes interval, at least 6 minutes
    """
    key_type_one = 1  # default interval one to (1)
    key_type_two = 2  # default interval two to (2)
    key_type_thr = 3  # default interval three to (3)

    def __init__(self):
        self._config = {attr: getattr(conf, attr) for attr in dir(conf) if attr[0].isupper()}
        self._default_news_root = self._config['DEFAULT_CSF_NEWS']

    @staticmethod
    def timestamp(datetime_str):
        year = datetime_str[:4]
        month = datetime_str[4:6]
        day = datetime_str[6:8]
        hour = datetime_str[8:10]
        minute = datetime_str[10:12]
        second = datetime_str[12:]
        time_str = '%s-%s-%s %s:%s:%s' % (year, month, day, hour, minute, second)

        try:
            return time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
        except ValueError:
            pass

    @staticmethod
    def get_domain_pubdate(file_path, yesterday):
        with open(file_path) as fp:
            url, pub_date = fp.readlines()[:2]
            if int(pub_date.strip()) and pub_date.startswith(yesterday):
                domain = tld.get_tld(url.strip(), as_object=True).domain
                return domain, pub_date.strip()
        return None, None

    @property
    def walk(self):
        """ 函数返回值是各网站在各时间段组成的字典 如：{domain: {1: [timestramp1, timestramp2, ...]}}"""
        mtime_dict = defaultdict(lambda: defaultdict(list))
        yesterday = str(date.today() - timedelta(days=1)).replace('-', '')
        news_path = self._default_news_root + yesterday + '/'
        print news_path

        for root, dirs, files in os.walk(news_path):
            for filename in files:
                domain, pub_date = self.get_domain_pubdate(root + filename, yesterday)

                if domain and len(pub_date) == 14:
                    required_time = int(pub_date[8:12])
                    timestramp = self.timestamp(pub_date)

                    if timestramp:
                        if 600 <= required_time <= 1000:
                            default_key = self.key_type_one
                        elif 1000 < required_time < 2000:
                            default_key = self.key_type_two
                        else:
                            default_key = self.key_type_thr
                        mtime_dict[domain][default_key].append(timestramp)
        return mtime_dict

    @property
    def intervals(self):
        """
        将前一天的历史新闻的发布时间戳按顺序相减，去除最大值和最小值得到两条新闻的平均发布时间间隔
        """
        mtime_dict = self.walk
        intervals_dict = defaultdict(defaultdict)

        for domain, defaulte_dict in mtime_dict.iteritems():
            for _default_key, _timestramp_list in defaulte_dict.iteritems():
                time_sorted = sorted(_timestramp_list)
                _intervals = map(lambda x, y: (x - y), time_sorted[1:], time_sorted[:-1])

                # Default remove the highest and lowest number
                intervals = sorted(_intervals)[1:-1]

                if not intervals:
                    default_interval = self.default_interval[_default_key]
                else:
                    div, mod = divmod(sum(intervals) / len(intervals), 60)
                    default_interval = self.rule_interval(int(div + (mod and 1)), _default_key)
                intervals_dict[domain][_default_key] = default_interval
            self.add_default_interval(intervals_dict[domain])  # add this site default interval to this period of time
        return intervals_dict

    @property
    def default_interval(self):
        return {1: 5, 2: 8, 3: 10}

    def add_default_interval(self, default):
        default.setdefault(self.key_type_one, self.default_interval[self.key_type_one])
        default.setdefault(self.key_type_two, self.default_interval[self.key_type_two])
        default.setdefault(self.key_type_thr, self.default_interval[self.key_type_thr])

    def rule_interval(self, interval, default_key):
        max_min_interval = {
            self.key_type_one: {'max': 5, 'min': 2},
            self.key_type_two: {'max': 8, 'min': 3},
            self.key_type_thr: {'max': 10, 'min': 6},
        }

        imax = max_min_interval[default_key]['max']
        imin = max_min_interval[default_key]['min']

        if imin <= interval <= imax:
            return interval
        elif interval < imin:
            return imin
        else:
            return imax


class BaseSched(object):
    def __init__(self):
        self._config = news_config

    @property
    def overall_sites(self):
        domain_sites = defaultdict(list)

        for site in self._config.names:
            domain_sites[site.split('_')[1]].append(site)
        return domain_sites

    @staticmethod
    def schedule(project='news_spiders', spider='news', settings=None, **kwargs):
        ScrapydAPI().schedule(project=project, spider=spider, settings=settings, **kwargs)

    def dispatch_job(self, default_type, interval, kw_values):
        _kwargs = {'site_name': kw_values}

        if default_type == 1:
            # 默认间隔为 5 分钟
            app.add_job(self.schedule, trigger='interval', kwargs=_kwargs, minute=interval, hour='6-9')

        if default_type == 2:
            # 默认间隔为 8 分钟
            app.add_job(self.schedule, trigger='interval', kwargs=_kwargs, minute=interval, hour='10-19')

        if default_type == 3:
            # 默认间隔为 10 分钟
            app.add_job(self.schedule, trigger='interval', kwargs=_kwargs, minute=interval, hour='20-23,0-5')

