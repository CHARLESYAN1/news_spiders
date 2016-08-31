# -*- coding: utf-8 -*-

import re

SANBAN_CONFIGS = [
    {
        'site': 'sanban_hexun',
        'urls': [
            {
                'page_url': 'http://stock.hexun.com/xsbyw/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.temp01', ),
        'remove_tags': ('[style="text-align:right;font-size:12px"]', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#artibody', )
            }
    },

    {
        'site': 'sanban_10jqka',
        'urls': [
            {
                'page_url': 'http://stock.10jqka.com.cn/xinsanban/sanban_list/index%s.shtml',
                'pages': 1, 'first': '',  'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('h2', ),
        'remove_tags':  ('#editor_baidu', 'p[style="text-align:center;"]'),
        'details':
            {
                'pyq_title':        ('.articleTit', ),
                'pyq_date_author': {
                    'date': (".fromNews", ),
                    'auth': ('#sourcename', )
                },
                'pyq_content':      ('.art_main', )
            }
    },

    {
        'site': 'sanban_sina',
        'urls': [
            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/zq1/sbsc/index_%s.shtml',
                'pages': 1, 'first': '%s',  'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.list_009', ),
        'remove_tags': ('.img_descr', '#sinashareto', '.finance_app_zqtg',  '.otherContent_01',
                        '.hqimg_related', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', ),
                'pyq_date_author':  {
                    'date': ('.time-source', '#pub_date', '.titer'),
                    'auth': ('[data-sudaclick="media_name"]', '#media_name', '.source', )
                },
                'pyq_content':  (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S),
                                 '#artibody')
            }
    },

    {
        'site': 'sanban_cnfol',
        'urls': [
            {
                'page_url': 'http://sbsc.stock.cnfol.com/xsbyw/index%s.shtml',
                'pages': 1, 'first': '',  'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'multi_page':   ('#page',),
        'block_attr':   ('.NewsLstItem', '.text-pic-tt', ),
        'details':
            {
                'pyq_title':        ("#Title", ),
                'pyq_date_author': {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#Content', )
            }
    },

    {
        'site': 'sanban_ifeng',
        'urls': [
            {
                'page_url': 'http://finance.ifeng.com/stock/special/xinsanban/index.shtml%s',
                'pages': 1, 'first': '',  'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.Nlis_01', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('#artical_topic', ),
                'pyq_date_author':  {
                    'date': (('#artical_sth', 'p'), ),
                    'auth': ('[ref="nofollow"]', )
                },
                'pyq_content':      ('#artical_real', )
            }
    },

    {
        'site': 'sanban_stcn',
        'urls': [
            {
                'page_url': 'http://yq.stcn.com/xsb/%s.shtml',
                'pages': 1, 'first': '%s',  'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.maj_box_list', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        (('h2', 0),),
                'pyq_author_date':  {
                    'date': (('.content_tit', 'span'), ),
                    'auth': (('.content_tit', 'p'), ),
                },
                'pyq_content':      ('#ctrlfscont', )
            }
    },

    {
        'site': 'sanban_asiafinance',
        'urls': [
            {
                'page_url': 'http://stock.asiafinance.cn/list/list_sanb%s.shtml',
                'pages': 1, 'first': '',  'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'multi_page':   (('.pagelist', 1), ),
        'block_attr':   ('.listCont', ),
        'remove_tags': ('.selectDiv', ),
        'details':
            {
                'pyq_title':        (('h1', 0),),
                'pyq_date_author':  {
                    'date': ('.zi2', ),
                    'auth': ('.zi2', ),
                },
                'pyq_content':      ('.content', )
            }
    },

    {
        'site': 'sanban_p5w',
        'urls': [
            {
                'page_url': 'http://www.p5w.net/stock/news/xsb/index%s.htm',
                'pages': 1, 'first': '',  'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.title', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('.title', ),
                'pyq_author_date':  {
                    'date': ('.source', ),
                    'auth': ('.source', ),
                },
                'pyq_content':  ('.text', )
            }
    },

    {
        'site': 'sanban_xsbdzw',
        'urls': [
            {
                'page_url': 'http://www.xsbdzw.com/html/qyly/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },

            {
                'page_url': 'http://www.xsbdzw.com/html/xwdt/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.newslist', ),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.time', ),
                    'auth': ('.time', ),
                },
                'pyq_content':  ('div[class="content"]', )
            }
    },

    {
        'site': 'sanban_sanban18',
        'urls': [
            {
                'page_url': 'http://www.sanban18.com/Industry/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },

            {
                'page_url': 'http://www.sanban18.com/news/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('h3', ),
        'remove_tags':  ('#hits', ),
        'details':
            {
                'pyq_title':        ('.tt-news', ),
                'pyq_date_author':  {
                    'date': ('.news-from', ),
                    'auth': ('.bule', )
                },
                'pyq_content':  ('.newscont', )
            }
    },

    {
        'site': 'sanban_21so',
        'urls': [
            {
                'page_url': 'http://stocks.21so.com/gongsi/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.title', '.freshNewsList'),
        'remove_tags': ('.goindex', ),
        'details':
            {
                'pyq_title':        ('.artcleTitle',),
                'pyq_date_author':  {
                    'date': ('.articleDate',),
                    'auth': ('.articleSource',)
                },
                'pyq_content':      ('.articleContentTD', )
            }
    },

    {
        'site': 'sanban_17ok',
        'urls': [
            {
                'page_url': 'http://stock.17ok.com/list.php?id=1110%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'block_attr':   ('.list', ),
        'details':
            {
                'pyq_title':        (('h2', 1), ),
                'pyq_date_author':  {
                    'date': ('h5', ),
                    'auth': ('h5', ),
                },
                'pyq_content':      ('.arti-con', )
            }
    },

    {
        'site': 'full_3bf',
        'urls': [
            {
                'page_url': 'http://3bf.cc/home/ajax/channel_index?offset=0&limit=30%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'新三板'
            },
        ],
        'json': {
            'data_key': 'data',
            'url_key': 'id',
            'join_key': 'http://3bf.cc/a/update/{url}'
        },
        'remove_tags': (),
        'details':
            {
                'pyq_title': ('div[class="title f-cb"]',),
                'pyq_date_author': {
                    'date': ('div.source span.time',),
                    'auth': (),
                },
                'pyq_content': ('div.m-info_conten div.conten', )
            }
    },

]
