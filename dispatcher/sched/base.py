# -*- coding: utf-8 -*-
import os
import time
import os.path
from os.path import abspath as _abs
from collections import defaultdict
from datetime import date, timedelta
from multiprocessing.dummy import Pool as ThreadPool

import tld
from scrapyd_api import ScrapydAPI

from . import conf
from .. import app, logger
from news_spiders.conf import news_config


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
        # self._overall_sites = self._config.names

    @property
    def is_migrate(self):
        return self._config.settings['IS_MIGRATE']

    @property
    def most_sites(self):
        domain_sites = defaultdict(list)

        for _config in self._config.most_configs:
            site_name = _config.get('site')

            if site_name:
                domain_sites[site_name.split('_')[1]].append(site_name)
        return domain_sites

    @property
    def hot_sites(self):
        return [_conf['site'] for _conf in self._config.hot_configs if _conf.get('site')]

    @property
    def sgp_sites(self):
        return [_conf['site'] for _conf in self._config.amazon_configs if _conf.get('site')]

    @property
    def scrapyd_host(self):
        return self._config.settings.get('SCRAPYD_HOST')

    def schedule(self, project='news_spiders', spider='news', settings=None, **kwargs):
        site_names = kwargs.get('site_name', [])
        sites = site_names if isinstance(site_names, (list, tuple)) else [site_names]
        _schedule = (
            lambda _site_name:
            ScrapydAPI(self.scrapyd_host).schedule(
                project=project,
                spider=spider,
                settings=settings,
                site_name=_site_name
            )
        )

        pool = ThreadPool(12)
        pool.map(_schedule, sites)
        pool.close()
        pool.join()

    def dispatch_job(self, default_type, interval, kw_values):
        """
        dispatch jobs by `default_type` and `interval`
        :param default_type: int, dispatch job type
        :param interval: int, interval time
        :param kw_values: dict, site name
        """

        interval = '*/%s' % interval
        _kwargs = {'site_name': kw_values}

        if default_type == 1:
            # 全量分派任务， 默认间隔为 5 分钟
            hour = '6-9'
        elif default_type == 2:
            # 全量分派任务， 默认间隔为 8 分钟
            hour = '10-19'
        elif default_type == 3:
            # 全量分派任务， 默认间隔为 10 分钟
            hour = '20-23,0-5'
        else:
            logger('full jobs schedule time type <{}> failed: <>'.format(default_type, _abs(__file__)))
            raise
        app.add_job(self.schedule, trigger='cron', kwargs=_kwargs, minute=interval, hour=hour, misfire_grace_time=10)

