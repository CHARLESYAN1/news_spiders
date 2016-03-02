# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import os
import logging
import platform

DB_PORT = 27017
DB_NAME = 'news_crawl'
DB_HOST = '192.168.0.223'
HOT_COLLECTION = 'hot_news'
DB_COLLECTION = 'finance_news_all'
PATCH_COLLECTION = 'sum_news'

PUSH_HOST = '10.0.3.10'
PUSH_PWD = ''

MAIN_PROCESS_LIMIT = 12
CHILD_THREAD_LIMIT = 50

# Office Shanghai env ip
OFFICE_SH_IP = '192.168.250.207'

# Office Shanghai test ip
TEST_SH_IP = '192.168.0.233'

# Amazon Beijing ip
AMAZON_BJ_IP = '10.0.3.11'

# Amazon Singapore
AMAZON_SG_IP = '10.148.157.46'

_deploy_ip = local_ip()

if _deploy_ip == OFFICE_SH_IP:
    IS_MIGRATE = False
    CONSOLE_LOG_LEVEL = logging.INFO
elif _deploy_ip == AMAZON_BJ_IP:
    IS_MIGRATE = True
    CONSOLE_LOG_LEVEL = logging.INFO
elif _deploy_ip == AMAZON_SG_IP:
    IS_MIGRATE = None
    CONSOLE_LOG_LEVEL = logging.INFO
elif _deploy_ip == TEST_SH_IP:
    IS_MIGRATE = False
    CONSOLE_LOG_LEVEL = logging.INFO
else:
    # Mainly to PC
    IS_MIGRATE = False
    CONSOLE_LOG_LEVEL = logging.DEBUG

# `sys.platform` could also know system platform
# know this system belong to which OS which
PLATFORM = platform.system().lower()[:3] == 'win'
CONFIG_DISPATCH = os.path.join(os.path.dirname(__file__), 'dispatch.cfg')
CONFIG_GENERIC = os.path.join(os.path.dirname(__file__), 'sched.cfg')

# 早高峰, 晚高峰, 对所有新闻， 包括热点和全量
MORNING_PEAK = ('08:00', '10:00')
EVENING_PEAK = ('15:00', '17:00')
HP_INTERVAL = '4m'  # hot news interval at peak
FP_INTERVAL = '8m'  # full news interval at peak
HH_INTERVAL = '15m'  # hot news interval at holiday
FH_INTERVAL = '20m'  # full news interval at holiday

# IP, The file transfer to redis, supply analysis server for data analysis
ANALYSIS_IP = '54.223.46.84'

# Redis channel to transfer full news
NEWS_CHANNEL = 'csf_news'

# Redis channel to transfer hot news
HOT_CHANNEL = 'csf_hot'

# Redis to transfer sgp news to office 207 env or Amazon beijing env
SGP_HOT = 'sgp_hot'  # hot news pub/sub channel
SGP_NEWS = 'sgp_news'  # others news, including full news pub/sub channel
SGP_HOT_MQ = 'sgp_hot_mq'  # hot news message queue
SGP_NEWS_MQ = 'sgp_news_mq'  # others news, including full news message queue

# make news content paragraph
LINE_BREAK = u'#&#'

# Redis relative config
if IS_MIGRATE is True:
    REDIS_HOST = 'localhost'
else:
    REDIS_HOST = '54.223.52.50'

REDIS_FILTER_KEY = 'url_tit_key'

# Basic store path config
if PLATFORM:
    HOT_FILE_OR_FILE__DB_PATH = 'D:/temp/dbs/'
    PATCH_FILE_DB_PATH = 'D:/temp/dbs/'
    NEWS_DIR_PATH = 'D:/temp/csf_news/'
    HOT_ORI_NEWS_PATH = 'D:/temp/hot_ori_news/'
    HOT_DES_NEWS_PATH = 'D:/temp/hot_des_news/'
else:
    # HOT_FILE_OR_FILE__DB_PATH = '/opt/news_analyse/full_news_one/dbs/'
    _bsd_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    HOT_FILE_OR_FILE__DB_PATH = os.path.join(_bsd_dir, 'dbs/')
    PATCH_FILE_DB_PATH = '/home/xutaoding/temp/data/'

    if IS_MIGRATE or IS_MIGRATE is None:
        NEWS_DIR_PATH = '/data/news/csf_news/'
        HOT_ORI_NEWS_PATH = '/data/news/csf_hot_news/'
        HOT_DES_NEWS_PATH = '/data/news/csf_hot_news/'
    else:
        NEWS_DIR_PATH = '/data/news_analyse/daily_news/csf_news/'
        HOT_ORI_NEWS_PATH = '/data/news_analyse/daily_news/csf_hot_temp/'
        HOT_DES_NEWS_PATH = '/data/news_analyse/daily_news/csf_hot_news/'

# For full news, title need to filter these keywords, and mark 1
TITLE_KEYS_FILTER = {
    "start": [u"网易机构预测", u"一致预期", u"中证数据", u"宁波海顺", u"倍新咨询", u"巨丰投顾", u"股商财富报告",
              u"南京证券", u"股市在线", u"专家预测", u"港股精选", u"国企指数", u"技术分析", u"权重股",
              ],

    "end": [u"一览", u"一览表", u"汇总", u"）", u")", u"文字实录", u"金股", u"成长股", u"停牌", u"个股"],

    "in":  [u'附股', u"公告", u"恒指", u"沪指", u"A股", u"a股", u"大盘", u"涨停", u"跌停",  u"多头",  u"空头",
            u"板块", u"蓝筹", u"杀跌", u"庄股", u"冲高回落", u"机构看后市", u"券商股", u"概念股", u"牛市",
            u"熊市", u"成长股", u"市场前瞻", u"权重股", u"保险股", u"金融股", u"停牌", u"调仓", u"个股",
            u"尾盘", u"连阴", u"头条汇编", u'精华摘要', u'千股千评', u'股海导航', u'受益股', u'名单', '掘金路线',
            u'交易提示', u'龙虎榜', u'个股揭秘', u'附名单', u'更新中', u'个股追踪', u'技术选股', u'研报精选',
            u'午评', u'宏观经济每日要闻', u'开盘', u'盘前', u'早盘必读', u'新闻速读', u'操作策略',  u'收盘分析',
            u'看盘', u'创业板指', u'中小板指', u'反弹', u'三大猜想', u'券商评级', u'机构荐股', u'机构推荐',
            u'券商策略', u'行情', u'机构新动向', u'牛股', u'十字星', u'资金离场', u'收评', u'异常股',  u'异动股'
            ],

    "start_regex": [re.compile(r"\d+月\d+日"), re.compile(r'\d{2}00点')],
    "end_regex": [],
    "ind_regex": [re.compile(r"\d+月\d+日"), ],
}

# For hot news, title need to filter these keywords, and mark 1
HOT_KEYS_FILTER = {
    "start": [u'快讯', u'盘前必读', u'白话股市', u'隔夜国际市场'],
    "end":   [],
    "in":   [u'附股', u'午评', u'收盘', u'重磅消息', u'汇总', u'早餐精选', u'要闻必读', u'要闻集萃',
             u'组图', u'千股千评',  u'股海导航', u'受益股', u'名单', '掘金路线', u'交易提示', u'龙虎榜',
             u'个股揭秘', u'附名单', u'更新中', u'个股追踪', u'技术选股', u'研报精选', u'宏观经济每日要闻',
             u'开盘', u'盘前', u'早盘必读', u'新闻速读', u'操作策略', u'收盘分析', u'看盘', u'创业板指',
             u'中小板指', u'反弹', u'三大猜想', u'券商评级', u'机构荐股', u'机构推荐', u'券商策略', u'行情',
             u'机构新动向', u'牛股', u'十字星', u'资金离场', u'收评', u'异常股', u'异动股', u'简报'
             ],

    "start_regex": [re.compile(r"\d+月\d+日"), re.compile(r'\d{2}00点')],
    "end_regex": [],
    "ind_regex": [],
}

# In generally, this text locate end with news content
# In news content, some text is redundant and some keywords impact analysis in some web sites
ENDSWITH_TEXT = {
    'qq':           [u'微信扫一扫', u'扫描二维码', u'更多精彩内容欢迎搜索关注微信'],
    'wallstreetcn': [u'（更多精彩财经资讯，点击这里下载华尔街见闻App'],
    'emoney':       ['当前行情下投资者需紧跟主力步伐', ],
    'kxt':          ['（本文原文出自', '（更多精彩财经资讯']
}

# In generally, this text locate middle with news content
# In news content, some text will impact analysis in some web sites, need to get rid of
SUB_TEXT = {
    # Need replace text to add parentheses
    '17ok': [u'\(\d{6}(，股吧)\)']
}

# Some web sites without source, but can I take a link to determine
URL_DETERMINE_AUTH = {
    'qq': '棱镜',  # 热点新闻， hjd 均有
    'cbrc': '银监会',
    'mof': '国务院',
    'jiemian': '界面',
    'emoney': '益盟财经',
    'kxt': '快讯通财经',
    'meigu18': '美股王',
    'pbc': '中国人民银行',
    'opsteel': '欧浦智网',
    'cnforex': '环球外汇',
    'thepaper': '澎湃新闻',
    'zaobao': '联合早报网',
    'ftchinese': 'FT中文网',
    'chiefgroup': '致富证券',
    'cailianpress': '财联社',
    'brandcn': '品牌中国网',
    'reuters': '路透社中文网',
    'wsj': '华尔街日报中文网',
    'nytimes': '纽约时报中文网',
    'wallstreetcn': '华尔街见闻',
    'chineseworldnet': '环球财经',
    'forbeschina': '福布斯中文网',
}

# multi page text, when you get all links, there are some links you don't need
MULTI_URI_TRASH = {
    'ftchinese': {'page=rest', 'full=y'}
}

# For frequency, Maybe you need it
HOLIDAY_CONFIGS = {
    # workday key is weekend, but on duty according to the national law
    'workday': {'2016-02-06', '2016-02-14', '2016-06-12', '2016-09-18', '2016-10-08', '2016-10-09'},

    # holiday key is weekday, but not on duty according to the national law
    'holiday': {
        '2016-01-01', '2016-02-08', '2016-02-09', '2016-02-10', '2016-02-11', '2016-02-12',
        '2016-04-04', '2016-05-02', '2016-06-09', '2016-06-10', '2016-09-15', '2016-09-16',
        '2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07',
    }
}

USER_AGENT = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) '
                   'AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'},

    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:42.0) Gecko/20100101 Firefox/42.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'}
]

