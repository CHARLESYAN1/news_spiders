# -*- coding: utf-8 -*-

import re

HK_CONFIGS = [
    {
        'site': 'hk_ifeng',
        'urls': [
            {
                'page_url':   'http://finance.ifeng.com/hk/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
             },
         ],
        'block_attr':   ('.box_01', '.col_new'),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('#artical_topic', ),
                'pyq_date_author':  {
                    'date': ('.ss01', ),
                    'auth': ('.ss03', )
                },
                'pyq_content':      ('#main_content', )
            }
    },

    {
        'site': 'hk_sina',
        'urls': [
            {
                'page_url':   'http://roll.finance.sina.com.cn/finance/gg/gsxw/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.list_009', ),
        'remove_tags': ('.img_descr', '.xb_new_finance_app', '.otherContent_01', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', ),
                'pyq_date_author':  {
                    'date': ('.time-source', ),
                    'auth': ('span[data-sudaclick="media_name"]',)
                },
                'pyq_content':  (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S), )
            }
    },

    {
        'site': 'hk_qq',
        'urls': [
            {
                'page_url':   'http://finance.qq.com/l/hk/ggxw/index%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.newslist', ),
        'remove_tags': ('.pictext', '#invideocon', '#relInfo', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.pubTime', ),
                    'auth': ('.where', ),
                },
                'pyq_content':      ('#Cnt-Main-Article-QQ', )
            }
    },

    {
        'site': 'hk_stcn',
        'urls': [
            {
                'page_url': 'http://hk.stcn.com/%s', 'pages': 1,
                'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('div[class="cnt_col1_box"]', ),
        'remove_tags':  ('.setFZ', ),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_date_author':  {
                    'date': ('.info', ),
                    'auth': ('.info', ),
                },
                'pyq_content':      ('#ctrlfscont', )
            }
    },

    {
        'site': 'hk_yicai',
        'urls': [
            {
                'page_url': 'http://www.yicai.com/markets/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('#newslist', ),
        'details':
            {
                'pyq_title':        (('h1', 0),),
                'pyq_author_date':  {
                    'date': (('h2', None, 0), ),
                    'auth': (('h2', None, 0), ),
                },
                'pyq_content':  ('.tline', )
            }
    },

    {
        'site': 'hk_ccstock',
        'urls': [
            {
                'page_url': 'http://www.ccstock.cn/gscy/hkgongsi/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.listMain', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_author_date':  {
                    'date': ('.sub_bt', ),
                    'auth': ('.sub_bt', ),
                },
                'pyq_content':      ('#newscontent', )
            }
    },

    {
        'site': 'hk_hexun',
        'urls': [
            {
                'page_url': 'http://hk.stock.hexun.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },

            {
                'page_url': 'http://stock.hexun.com/hknews/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('ul[class="text2a"][_extended="true"]', '.temp01'),
        'remove_tags': ('[style="text-align:right;font-size:12px"]', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':  ('#artibody', )
            }
    },

    {
        'site': 'hk_jrj',
        'urls': [
            {
                'page_url': 'http://hk.jrj.com.cn/list/hgxw%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },

            {
                'page_url': 'http://hk.jrj.com.cn/list/gsxw%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.jrj-l1',),
        'remove_tags': ('.pictext', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 1), ),
                'pyq_date_author':  {
                    'date': ('.inftop', ),
                    'auth': ('.inftop', ),
                },
                'pyq_content':      ('.texttit_m1', )
            }
    },

    {
        'site': 'hk_sohu',
        'urls': [
            {
                'page_url': 'http://stock.sohu.com/hk/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.list',),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author': {
                    'date': ('#pubtime_baidu', ),
                    'auth': ("#media_span", )
                },
                'pyq_content':      ('[itemprop="articleBody"]', )
            }
    },

    {
        'site': 'hk_money163',
        'urls': [
            {
                'page_url': 'http://money.163.com/hkstock/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.newslist_normal',),
        'remove_tags': (re.compile(r'<!--biaoqian.*?>.*?<!--biaoqian.*?>', re.S),
                        'div[class="ep-source cDGray"]', '.nvt_vote_2', '.demoBox',
                        '.hidden', '.nph_photo', '.nph_photo_ctrl', '.hidden', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_date_author': {
                    'date': ('.ep-time-soure', ),
                    'auth': ("#ne_article_source", )
                },
                'pyq_content':      ('#endText', )
            }
    },

    {
        'site': 'hk_cs',
        'urls': [
            {
                'page_url': 'http://www.cs.com.cn/gg/ggyw/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },

            {
                'page_url': 'http://www.cs.com.cn/gg/gsxw/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.column-box',),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.ctime', ),
                    'auth': (('.Atext', None, 1), )
                },
                'pyq_content':      ('#ozoom1', )
            }
    },

    {
        'site': 'hk_aastocks',
        'urls': [
            {
                'page_url': 'http://www.aastocks.com/sc/stocks/news/aafn/top-news/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },

            {
                'page_url': 'http://www.aastocks.com/sc/stocks/news/aafn-company-news/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },

            {
                'page_url': 'http://www.aastocks.com/sc/stocks/news/aafn/ipo-news/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },

            {
                'page_url': 'http://www.aastocks.com/sc/stocks/news/aafn-ind/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('.h6',),
        'details':
            {
                'pyq_title':        ('#lblSTitle', ),
                'pyq_date_author':  {
                    'date': ('#spanDateTime', ),
                    'auth': ('#spanDateTime', ),
                },
                'pyq_content':      ('#spanContent', )
            }
    },

    {
        'site': 'hk_finet',
        'urls': [
            {
                'page_url': 'http://www.finet.hk//mainsite/newscenter/PRNHKX/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },
        ],
        'block_attr':   ('.iallnewsboxs',),
        'remove_tags': ('[rel="nofollow"]',),
        'details':
            {
                'pyq_title':        ('#newstitle', ),
                'pyq_date_author':  {
                    'date': ('.titme', ),
                    'auth': ('.titme', ),
                },
                'pyq_content':      ('#contentArea', )
            }
    },

    {
        'site': 'hk_yahoo',
        'urls': [
            {
                'page_url': 'https://hk.finance.yahoo.com/news/all-stories/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/stock-news/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-hkej/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-singtao/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-singtao/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-thesun/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-hket/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-wsj/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-finet/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },

            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-aastocks/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hk'
            },
        ],
        'is_script': False,
        'block_attr':   (re.compile(r'class="txt".*?a href="(?P<url>.*?html)', re.S),),
        'details':
            {
                'pyq_title':        ('.headline', ),
                'pyq_date_author':  {
                    'date': (re.compile(r'datePublished.*?content=(.*?)Z', re.S), ),
                    'auth': (re.compile(r'itemprop="provider" content="(.*?)"', re.S), )
                },
                'pyq_content':      ('#mediaarticlebody', )
            }
    },

    {
        'site': 'hk_21so',
        'urls': [
            {
                'page_url': 'http://stocks.21so.com/ganggu/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
            },
        ],
        'block_attr':   ('[class="title"]',),
        'remove_tags': ('.goindex', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('.artcleTitle', ),
                'pyq_date_author':  {
                    'date': ('.articleDate', ),
                    'auth': ('.articleSource', )
                },
                'pyq_content':      ('.articleContentTD', )
            }
    },

    {
        'site': 'hk_21so',
        'urls': [
            {
                'page_url': 'http://stocks.21so.com/ganggu/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
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

    # {
    #     'site': 'hk_chiefgroup',
    #     'urls': [
    #         {
    #             'page_url': 'http://www.chiefgroup.com.hk/financialinfo/fi_marketnews.php%s',
    #             'sub_link': 'http://www.chiefgroup.com.hk/news_details.php?id=%s',
    #             'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'港股新闻'
    #         },
    #     ],
    #     'block_attr':   (re.compile(r'<tr class="table_bg.*?>.*?'
    #                                 r'<div align="center">(?P<date>.*?)</div>.*?'
    #                                 r'<a href="javascript:popup_news\(\'(?P<url>\d+)\'\)', re.S), ),
    #     'remove_tags': ('.goindex', ),
    #     'details':
    #         {
    #             'pyq_title':        ('td[height="30"][valign="middle"]',),
    #             'pyq_date_author':  {
    #                 'date': (),
    #                 'auth': ()
    #             },
    #             'pyq_content':      ('td[width="650"]', )
    #         }
    # },

]
