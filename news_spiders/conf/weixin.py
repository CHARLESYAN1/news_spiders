# -*- coding: utf-8 -*-
import re
import urllib

__remove_tags = (
    'span[style="font-size: 14px; max-width: 100%; box-sizing: border-box !important; word-wrap: break-word '
    '!important;"]',

    'span[style="font-size: 14px; max-width: 100% !important; box-sizing: border-box !important; '
    'word-wrap: break-word !important;"]',

    'span[style="font-size: 14px; max-width: 100%; box-sizing: border-box !important; '
    'word-wrap: break-word !important;"]',

    'strong[style="max-width: 100% !important; box-sizing: border-box !important; word-wrap: break-word '
    '!important;"]',

    'span[style="color: rgb(0, 0, 0); max-width: 100%; box-sizing: border-box !important; '
    'word-wrap: break-word !important;"]',

    'span[style="color: inherit; font-family: inherit; font-size: 1.2em; line-height: 1.6; '
    'text-decoration: inherit;"]',

    'strong[style="font-size: 14px; line-height: 25.6px;"]',

    'p[style="margin-bottom: 10px; line-height: normal;"]',
)

SECURITY_CONFIGS = [
    {
        'site': 'wx_zszq',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('浙商证券研究所'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'), ),
        'block_attr':   ('h4.weui_media_title', ),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title':        ('h2#activity-name', ),
                'pyq_author_date':  {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S), ),
                    'auth': ('a#post-user', ),
                },
                'pyq_content':  ('div#js_content', )
            },

        'beat': {'trigger': 'cron', 'minute': '15,30', 'hour': '7'}
    },

    {
        'site': 'wx_htzq',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('华泰证券研究所'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '10,20', 'hour': '9'}
    },

    {
        'site': 'wx_ztzq',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('中泰证券研究所'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '9'}
    },

    {
        'site': 'wx_gjzq',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('国金证券研究所'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '10,20', 'hour': '10'}
    },

    {
        'site': 'wx_dhzq',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('东海证券研究所'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    },

    # {
    #     'site': 'wx_cxzk',
    #     'urls': [
    #         {
    #             'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
    #             'first': urllib.quote('茶溪智库'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
    #         },
    #     ],
    #     'belong': 'weixin',
    #
    #     # 采用selenium 来抓取， 需要根据元素的类型
    #     # location_tags: 查找进入文章的标签元素
    #     'is_script': True,
    #     'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
    #     'block_attr': ('h4.weui_media_title',),
    #     'remove_tags': __remove_tags,
    #     'details':
    #         {
    #             'pyq_title': ('h2#activity-name',),
    #             'pyq_author_date': {
    #                 'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
    #                 'auth': ('a#post-user',),
    #             },
    #             'pyq_content': ('div#js_content',)
    #         },
    #
    #     'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    # },

    {
        'site': 'wx_jqzx',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('机器之心'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    },

    {
        'site': 'wx_qy',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('钱眼'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    },

    {
        'site': 'wx_znjrg',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('智能金融狗'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    },

    {
        'site': 'wx_thscj',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('同花顺财经'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    },

    {
        'site': 'wx_qkljr',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('区块链新金融'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    },

    {
        'site': 'wx_fintech',
        'urls': [
            {
                'page_url': 'http://weixin.sogou.com/weixin?query=%s', 'pages': 1,
                'first': urllib.quote('FinTech情报局'), 'reverse': None, 'suffix': None, 'cate': u'微信文章'
            },
        ],
        'belong': 'weixin',

        # 采用selenium 来抓取， 需要根据元素的类型
        # location_tags: 查找进入文章的标签元素
        'is_script': True,
        'location_tags': (('id', 'sogou_vr_11002301_box_0'),),
        'block_attr': ('h4.weui_media_title',),
        'remove_tags': __remove_tags,
        'details':
            {
                'pyq_title': ('h2#activity-name',),
                'pyq_author_date': {
                    'date': (re.compile(r'var ct = "(\d+?)";', re.S),),
                    'auth': ('a#post-user',),
                },
                'pyq_content': ('div#js_content',)
            },

        'beat': {'trigger': 'cron', 'minute': '15,25', 'hour': '10'}
    },
]
