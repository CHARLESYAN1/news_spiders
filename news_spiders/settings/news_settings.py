# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import socket
import logging
import platform

# 关于配置文件， 必须把测试环境和开发环境分开


def make_dev_ip():
    """
    :return: the actual ip of the local machine.
        This code figures out what source address would be used if some traffic
        were to be sent out to some well known address on the Internet. In this
        case, a Google DNS server is used, but the specific address does not
        matter much.  No traffic is actually sent.
    """
    try:
        _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _socket.connect(('8.8.8.8', 80))
        address, port = _socket.getsockname()
        _socket.close()
        return address
    except socket.error:
        return '127.0.0.1'

# ###################### AWS ##############################
# provide by wanjun
# AWS_ACCESS_KEY_ID = 'AKIAPY6JJ76F67VDOGBA'
# AWS_SECRET_ACCESS_KEY = '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'

# provide by jim
AWS_ACCESS_KEY_ID = 'AKIAO3EUM454XIVNARNA'
AWS_SECRET_ACCESS_KEY = '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'

AWS_HOST = 's3.cn-north-1.amazonaws.com.cn'
BUCKET_NAME = 'cn.com.chinascope.news'
# ###################### AWS ##############################

# #################### config module name ######################
HOT_CONFIGS_MODULE = 'news_spiders.conf.chot'
FULL_CONFIGS_MODULE = 'news_spiders.conf.cfull'
FUND_CONFIGS_MODULE = 'news_spiders.conf.cfund'
HK_CONFIGS_MODULE = 'news_spiders.conf.chk'
HIF_CONFIGS_MODULE = 'news_spiders.conf.chif'
SANBAN_CONFIGS_MODULE = 'news_spiders.conf.csanban'
USA_CONFIGS_MODULE = 'news_spiders.conf.cusa'
AMAZON_CONFIGS_MODULE = 'news_spiders.conf.camazon'
COMMENTS_CONFIGS_MODULE = 'news_spiders.conf.cguping'

SECURITY_CONFIGS_MODULE = 'news_spiders.conf.security'

SPECIFIC_CONFIGS = 'HOT_CONFIGS_MODULE, AMAZON_CONFIGS_MODULE, SECURITY_CONFIGS_MODULE'
# #################### module config ######################

# IP description
OFFICE_SH_IP = '192.168.250.207'    # Office Shanghai env ip
TEST_SH_IP = '192.168.0.233'        # Office Shanghai test ip
AMAZON_BJ_IP = '10.0.3.11'          # Amazon Beijing ip, that is intranet, the network is 54.223.52.50
AMAZON_SG_IP = '10.148.157.46'      # Amazon Singapore ip, that is intranet, the network is 54.251.56.190
ANALYSIS_IP = '54.223.46.84'        # Analysis server ip

_deploy_ip = make_dev_ip()

if _deploy_ip == OFFICE_SH_IP:
    IS_MIGRATE = False
elif _deploy_ip == AMAZON_BJ_IP:
    IS_MIGRATE = True
elif _deploy_ip == AMAZON_SG_IP:
    IS_MIGRATE = None
elif _deploy_ip == TEST_SH_IP:
    IS_MIGRATE = False
else:
    # Mainly to PC
    IS_MIGRATE = False

# `sys.platform` could also know system platform
# know this system belong to which OS which
PLATFORM = platform.system().lower()[:3].upper() == 'WIN'

# Redis Channel between amazon beijing server and sgp server
NEWS_CHANNEL = 'csf_news'   # transfer full news
HOT_CHANNEL = 'csf_hot'     # transfer hot news

# Redis Queue to transfer sgp news to office 207 env or Amazon beijing env
SGP_HOT = 'sgp_hot'  # hot news pub/sub channel
SGP_NEWS = 'sgp_news'  # others news, including full news pub/sub channel
SGP_HOT_MQ = 'sgp_hot_mq'  # hot news message queue
SGP_NEWS_MQ = 'sgp_news_mq'  # others news, including full news message queue

# Scrapyd Deploy host and port
if IS_MIGRATE is False:
    SCRAPYD_HOST = 'http://192.168.0.233:6800'
else:
    SCRAPYD_HOST = 'http://localhost:6800'

# make news content paragraph
LINE_BREAK = u'#&#'

# Redis relative config
if IS_MIGRATE is None:
    REDIS_HOST = '54.223.52.50'
else:
    REDIS_HOST = 'localhost'
REDIS_FILTER_KEY = 'url_tit_key'            # Filtering url and title md5
SCRAPY_FILTER_KEY = 'scrapy:url_filter'     # Sscrapy filter url and title md5
SCRAPY_PROXY_IP_KEY = 'scrapy:proxy_ip'     # Scrapy Queue to store proxy ip

# beijing amazon mongo config
AMAZON_BJ_MONGO_PORT = 27017
AMAZON_BJ_MONGO_HOST = '192.168.100.20' if IS_MIGRATE is False else ['10.0.250.10', '10.0.250.12']
AMAZON_BJ_MONGO_DB = 'news_crawl' if IS_MIGRATE is False else 'news'
AMAZON_BJ_MONGO_TABLE = 'hotnews_analyse'
AMAZON_BJ_MONGO_CRAWLER = 'crawler_news'

ANALYSIS_SERVER_INNER_IP = '192.168.250.207' if IS_MIGRATE is False else '10.0.3.10'
ANALYSIS_SERVER_PASSWORD = 'chinascope' if IS_MIGRATE is False else 'chinascope'

# Basic store path config
if PLATFORM:
    NEWS_DIR_PATH = 'D:/temp/csf_news/'
    HOT_ORI_NEWS_PATH = 'D:/temp/hot_ori_news/'
    HOT_DES_NEWS_PATH = 'D:/temp/hot_des_news/'

    LOG_PATH = 'D:/temp/news_log/'  # local log on win
    LOG_LEVEL = logging.DEBUG  # local log level on win

    PHANTOMJS_PATH = 'C:\Python27\Scripts\phantomjs.exe'
else:
    NEWS_DIR_PATH = '/data/news/csf_news/'
    HOT_ORI_NEWS_PATH = '/data/news/csf_hot_news/'
    HOT_DES_NEWS_PATH = '/data/news/csf_hot_news/'

    LOG_PATH = '/opt/news_log/'  # local log on linux
    LOG_LEVEL = logging.INFO  # local log level on linux

    PHANTOMJS_PATH = '/opt/source/src/phantomjs-1.9.7-linux-x86_64/bin/phantomjs'

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
    'kxt':          ['（本文原文出自', '（更多精彩财经资讯'],
    'ifeng':        ['大势解读'],
    'weixin':       ['欢迎关注']
}

# In generally, this text locate middle with news content
# In news content, some text will impact analysis in some web sites, need to get rid of
SUB_TEXT = {
    # Need replace text to add parentheses
    '17ok': [u'\(\d{6}(，股吧)\)']
}

# Discard the Article according to title
DISCARD_TITLE_ARTICLE = [
    '邀请培训', '电话会议', '培训纪要'
]

# Some web sites without source, but can I take a link to determine
URL_DETERMINE_AUTH = {
    'qq': '棱镜',  # 热点新闻， hjd 均有
    'cbrc': '银监会',
    'mof': '国务院',
    'jiemian': '界面',
    'p5w': '全景网',
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
PAGE_URI_TRASH = {
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


