# -*- coding: utf-8 -*-

import re

COMMENTS_CONFIGS = [
    {
        'site': 'gp_ifeng',
        'urls': [
            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/41/48/%s/dynlist.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.box_list',),
        'remove_tags': ('.picIntro', 'p[style="text-align: center;"]', 'span[style="color: rgb(128, 128, 128);"]'),
        'details':
            {
                'pyq_title': ('#artical_topic',),
                'pyq_date_author': {
                    'date': ('.ss01',),
                    'auth': ('.ss03',)
                },
                'pyq_content': ('#main_content',)
            }
    },

    {
        'site': 'gp_sina',
        'urls': [
            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/zq1/gsjsy/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },

            {
                'page_url': 'http://finance.sina.com.cn/stock/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.list_009',),
        'remove_tags': ('.img_descr', '#sinashareto', '.finance_app_zqtg', '.otherContent_01',
                        '.hqimg_related', 'style', 'script'),
        'details':
            {
                'pyq_title': ('#artibodyTitle',),
                'pyq_date_author': {
                    'date': ('.time-source', '#pub_date', '.titer'),
                    'auth': ('[data-sudaclick="media_name"]', '#media_name', '.source', '.time-source')
                },
                'pyq_content': (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S), '#artibody')
            }
    },

    {
        'site': 'gp_qq',
        'urls': [
            {
                'page_url': 'http://stock.qq.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.layout1 .extra .main', ),
        'remove_tags': ('.img_descr', '#sinashareto', '.finance_app_zqtg', '.otherContent_01',
                        '.hqimg_related', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.pubTime', ),
                    'auth': ('.where', )
                },
                'pyq_content':  ('#Cnt-Main-Article-QQ', )
            }
    },

    {
        'site': 'gp_cnstock',
        'urls': [
            {
                'page_url': 'http://stock.cnstock.com/live/index/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr':   ('#zb-list', ),
        'remove_tags':  ('span[style="color: #333399"]',),
        'details':
            {
                'pyq_title':        ('h1.title', ('h1', 1)),
                'pyq_date_author':  {
                    'date': ('.timer', '.time'),
                    'auth': ('.source', ('.sub-title', 'strong', 0))
                },
                'pyq_content':      ('#qmt_content_div', )
            }
    },

    {
        'site': 'gp_eastmoney',
        'urls': [
            {
                'page_url': 'http://finance.eastmoney.com/news/cdfsd_%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.list', ),
        'remove_tags': ('.c_review', '.BodyEnd', re.compile(r'<span style="color:#ff0000">.*?</div>', re.S),
                        'p[style="text-align:right; font-size:12px; color:#666;"]', ),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.Info', ),
                    'auth': ()
                },
                'pyq_content':      ('#ContentBody', )
            }
    },

    {
        'site': 'gp_hexun',
        'urls': [
            {
                'page_url': 'http://stock.hexun.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ((".newsList.mt5", 0), (".firstNewsLi", 0), '.newsListTim.mt8.clearfix', ),
        'remove_tags': ('.c_review', 'div[style="text-align:right;font-size:12px"]', ),
        'details':
            {
                'pyq_title': ('#artibodyTitle', '.ArticleTitleText'),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', '.ArticleTitle', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':  ('#artibody', '#BlogArticleDetail')
            }
    },

    {
        'site': 'gp_cfi',
        'urls': [
            {
                'page_url': 'http://stock.cfi.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.gpyaowen', ),
        'details':
            {
                'pyq_title': ("#tdcontent > h1", ),
                'pyq_date_author':  {
                    'date': ('td[style="font-size:9pt;text-align:center;white-space:nowrap;padding:3px 0px 5px 3px"]',),
                    'auth': ('td[style="font-size:9pt;text-align:center;white-space:nowrap;padding:3px 0px 5px 3px"]',)
                },
                'pyq_content':  ('#tdcontent', )
            }
    },

    {
        'site': 'gp_jrj',
        'urls': [
            {
                'page_url': 'http://stock.jrj.com.cn/invest/scgc%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr':   ('.clm', ),
        'remove_tags': ('font', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 1), ),
                'pyq_date_author':  {
                    'date': ('.inftop', ),
                    'auth': ('.inftop', ),
                },
                'pyq_content': ('.texttit_m1', )
            }
    },

    {
        'site': 'gp_p5w',
        'urls': [
            {
                'page_url': 'http://www.p5w.net/stock/market/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr':   ('.news-list', ),
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
        'site': 'gp_caijing',
        'urls': [
            {
                'page_url': 'http://stock.caijing.com.cn/market/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.main_lt', ),
        'remove_tags': ('.ar_writer', '.ar_keywords',),
        'details':
            {
                'pyq_title':        ('#cont_title',),
                'pyq_date_author': {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',),
                },
                'pyq_content':      ('#the_content', )
            }
    },

    {
        'site': 'gp_stockstart',
        'urls': [
            {
                'page_url': 'http://stock.stockstar.com/list/1031_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },

            {
                'page_url': 'http://stock.stockstar.com/list/96_%s.shtml',
                'pages': 1, 'first': '1', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.listtable', ".listnews", ),
        'remove_tags': ('[class="tags"]', '.selectPg', '#Page'),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_date_author': {
                    'date': ('#pubtime_baidu', ),
                    'auth': ("#source_baidu", )
                },
                'pyq_content':      ('.article', )
            }
    },

    {
        'site': 'gp_sohu',
        'urls': [
            {
                'page_url': 'http://stock.sohu.com/dashiyanpan/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },

            {
                'page_url': 'http://stock.sohu.com/s2015/shuju/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.lc', ),
        'remove_tags': ('span[style="font-size: 12px;"]', 'script', 'style'),
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
        'site': 'gp_163',
        'urls': [
            {
                'page_url': 'http://money.163.com/stock/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.news_importent', ('.news_struct', 3)),
        'remove_tags': (re.compile(r'<!--biaoqian.*?>.*?<!--biaoqian.*?>', re.S),
                        'div[class="ep-source cDGray"]', '.nph_photo', '.nph_photo_ctrl',
                        '.nvt_vote_2', '.demoBox', '.hidden', 'script', 'style', '.otitle'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author': {
                    'date': ('.ep-time-soure', '.post_time_source'),
                    'auth': ("#ne_article_source", )
                },
                'pyq_content':      ('#endText', )
            }
    },

    {
        'site': 'gp_10jqka',
        'urls': [
            {
                'page_url': 'http://stock.10jqka.com.cn/hsdp_list/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr':   ('h2', 'span.arc-title'),
        'remove_tags':  ('#editor_baidu', 'a.backweb', 'script', 'style', '.gsrd-hidden.brokers_hidden'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author': {
                    'date': ("#pubtime_baidu", ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('.atc-content', '.art_main', )
            }
    },

    {
        'site': 'gp_huagu',
        'urls': [
            {
                'page_url': 'http://stock.huagu.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr': ('.hotNews', '.newsBox > .pad14', ),
        'remove_tags': ('.page', 'span[style="width:0;height:0;overflow:hidden;display:block;font:0/0 Arial"]', ),
        'details':
            {
                'pyq_title':        ('#h1-title', ),
                'pyq_date_author':  {
                    'date': ('.info', ),
                    'auth': ('.where', )
                },
                'pyq_content':      ('#div-article-content', )
            }
    },

    {
        'site': 'gp_cs',
        'urls': [
            {
                'page_url': 'http://www.cs.com.cn/gppd/zzkpd/01/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },
        ],
        'block_attr':   ('.column-box', ),
        'remove_tags': ('p[style="text-align: center"]', 'style', 'script', ),
        'details':
            {
                'pyq_title':        (('h1', 1), ),
                'pyq_date_author':  {
                    'date': ('.ctime01', ),
                    'auth': (('.Atext', None, 1), )
                },
                'pyq_content':      ('.Dtext', )
            }
    },
]
