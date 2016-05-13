# -*- coding: utf-8 -*-

import re

FUND_CONFIGS = [
    {
        'site': 'fund_eastmoney',
        'urls': [
            {
                'page_url': 'http://fund.eastmoney.com/news/cjjyw%s.html',
                'pages': 1, 'first': '_%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.eastmoney.com/news/cjjgd%s.html',
                'pages': 1, 'first': '_%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.eastmoney.com/news/cjjtzcl%s.html',
                'pages': 1, 'first': '_%s', 'reverse': None, 'suffix': '_%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.eastmoney.com/news/cjjgjfx%s.html',
                'pages': 1, 'first': '_%s', 'reverse': None, 'suffix': '_%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.eastmoney.com/news/cjjdjyb%s.html',
                'pages': 1, 'first': '_%s', 'reverse': None, 'suffix': '_%s', 'cate': u'基金新闻'
            },
        ],
        'multi_page':   ('div.Page',),
        'block_attr':   ('div.infos', ),
        'remove_tags': ('div.c_review', 'span[style="color:#ff0000"]', 'span[style="color:#FF0000"]',
                        'p[style="text-align:right; font-size:12px; color:#666;"]', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('.Info', ),
                    'auth': (('.Info', 'span', 1), )
                },
                'pyq_content': (re.compile(r'<div id="ContentBody".*?>(.*?)<div style="position', re.S),
                                '#ContentBody')
            }
    },

    {
        'site': 'fund_sina',
        'urls': [
            {
                'page_url': 'http://finance.sina.com.cn/fund/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/jj4/jjsy/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/jj4/jjyj/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/jj4/jjpl/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('div.hdline ', 'ul.list_009'),
        'remove_tags': ('.img_descr', '.otherContent_01', '.hqimg_related', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', ),
                'pyq_date_author':  {
                    'date': ('.time-source', ),
                    'auth': ('span[data-sudaclick="media_name"]', )
                },
                'pyq_content':      (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S),
                                     '#artibody')
            }
    },

    {
        'site': 'fund_qq',
        'urls': [
            {
                'page_url': 'http://finance.qq.com/c/jjyw_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('div.Q-tpWrap', ),
        'remove_tags': ('.pictext', '#invideocon', '#relInfo', 'table', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0),),
                'pyq_date_author':  {
                    'date': ('.pubTime', ),
                    'auth': ('.where', )
                },
                'pyq_content':      ('#Cnt-Main-Article-QQ', )
            }
    },

    {
        'site': 'fund_cnstock',
        'urls': [
            {
                'page_url': 'http://caifu.cnstock.com/list/jj_yenei_dongtai/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://caifu.cnstock.com/list/jj_gongsi_jvjiao/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url':  'http://caifu.cnstock.com/list/jj_chanping_jvjiao/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url':  'http://caifu.cnstock.com/list/jj_shidian/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url':  'http://caifu.cnstock.com/list/jj_yanjiu_baogao/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('ul.new-list.article-mini', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('h1.title', '.title-inner h1'),
                'pyq_date_author':  {
                    'date': ('.timer', '.time'),
                    'auth': ('.source', ('.sub-title', 'strong', 0))
                },
                'pyq_content':      ('#qmt_content_div', )
            }
    },

    {
        'site': 'fund_ccstock',
        'urls': [
            {
                'page_url': 'http://www.ccstock.cn/fund/jijindongtai/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://www.ccstock.cn/fund/jijinlunshi/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://www.ccstock.cn/fund/jijinfangtan/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('ul.list-lf-matter', ),
        'remove_tags': ('span.author', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_author_date':  {
                    'date': ('.sub_bt', ),
                    'auth': ('.sub_bt', ),
                },
                'pyq_content':      ('#newscontent', )
            }
    },

    {
        'site': 'fund_cnfol',
        'urls': [
            {
                'page_url': 'http://fund.cnfol.com/jijinjiaodian/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_0%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.cnfol.com/jijinkanshi/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_0%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.cnfol.com/jijindongtai/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_0%s', 'cate': u'基金新闻'
            },
        ],
        'multi_page': ('#page', ),
        'block_attr':   ('ul.NewsLstItem', ),
        'remove_tags': ('#editor_baidu', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#Title', ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#Content', )
            }
    },

    {
        # # news list pagination not have rule, history news need to specially handle.
        'site': 'fund_cfi',
        'urls': [
            {
                'page_url': 'http://fund.cfi.cn/BCA0A4127A4247A4250.HTML%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.cfi.cn/BCA0A4127A4247A4261.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.cfi.cn/BCA0A4127A4247A4257.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('td.zilanmu', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('td[width="40%"]', ),
                    'auth': ('td[width="40%"]', ),
                },
                'pyq_content': (re.compile(r'<!--newstext-->(.*?)<!--/newstext-->', re.S), )
            }
    },

    {
        'site': 'fund_jrj',
        'urls': [
            {
                'page_url': 'http://fund.jrj.com.cn/list/jjdt%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.jrj.com.cn/list/jjks%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.jrj.com.cn/list/plyj%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('.jrj-l1', ),
        'remove_tags': ('font', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h2', 0), ),
                'pyq_date_author':  {
                    'date': ('.inftop .time', ),
                    'auth': ('.inftop .urladd', ),
                },
                'pyq_content':      ('.texttit_m1', )
            }
    },

    {
        'site': 'fund_stockstar',
        'urls': [
            {
                'page_url': 'http://fund.stockstar.com/list/1293_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.stockstar.com/list/1297_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://fund.stockstar.com/list/1565_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('.newslist_content', ),
        'remove_tags': ('.tags', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ("#source_baidu", )
                },
                'pyq_content':      ('.article', )
            }
    },

    {
        'site': 'fund_fund123',
        'urls': [
            {
                'page_url': 'http://news.fund123.cn/16/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://news.fund123.cn/17/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://news.fund123.cn/19/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('ul.listarea.listadd', ),
        'remove_tags': ('#bdshare', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': (('.gray6', None, 1), ),
                    'auth': ("#span_copyfrom", )
                },
                'pyq_content':      ('#main_article', )
            }
    },

    {
        'site': 'fund_howbuy',
        'urls': [
            {
                'page_url': 'http://www.howbuy.com/news/c/2/203.htm?page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://www.howbuy.com/news/c/2/204.htm?page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://www.howbuy.com/news/c/2/207.htm?page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://www.howbuy.com/news/c/2/217.htm?page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('div.newsList', ),
        'remove_tags': ('ul[class="rt"]', 'font', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('.share-tools', ),
                    'auth': ('.share-tools', ),
                },
                'pyq_content':      ('#content', )
            }
    },

    {
        'site': 'fund_morningstar',
        'urls': [
            {
                'page_url': 'http://cn.morningstar.com/research/institution%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('#ctl00_ctl00_cphMain_cphArticleMain_GridView1', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 1), ),
                'pyq_date_author':  {
                    'date': ('.date', ),
                    'auth': ('.ar_author a', )
                },
                'pyq_content':      ('.ar_content', )
            }
    },

    {
        'site': 'fund_hexun',
        'urls': [
            {
                'page_url': 'http://funds.hexun.com/hotnews/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://funds.hexun.com/report/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://funds.hexun.com/fundmarket/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://funds.hexun.com/focus/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://funds.hexun.com/store/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://funds.hexun.com/qfii/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://funds.hexun.com/qdii/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '-%s', 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('.temp01', ),
        'remove_tags': ('div[style="text-align:right;font-size:12px"]', 'select', 'font', 'style', 'script'),
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
        'site': 'fund_hexun_mob',
        'platform': 'mob',
        'urls': [
            {
                'page_url': 'http://m.hexun.com/ajax/ajax_news_s1.php?id=101767368&pn=%s&pc=20',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('li', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('.pubdate', ),
                    'auth': ('.pubdate', ),
                },
                'pyq_content':      ('#newsArticle', )
            }
    },

    {
        'site': 'fund_chinafund',
        'urls': [
            {
                'page_url': 'http://www.chinafund.cn/tree/sjzx/jjzx_%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://www.chinafund.cn/tree/jjyw/jjyw_%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('.pagelist', ),
        'remove_tags': ('div[style="text-align:right;font-size:12px"]', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#title', ),
                'pyq_date_author':  {
                    'date': ('#time', ),
                    'auth': (),
                },
                'pyq_content':      ('#news_text', )
            }
    },

    {
        'site': 'fund_kjj',
        'urls': [
            {
                'page_url': 'http://news.kjj.com/html/jijin/shichangxinwen/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://news.kjj.com/html/jijin/jigouguandian/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr':   ('#table_news', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('h3', ),
                'pyq_date_author':  {
                    'date': ('.copyfrom', ),
                    'auth': (),
                },
                'pyq_content':      ('.text', )
            }
    },

    {
        'site': 'fund_chnfund',
        'urls': [
            {
                'page_url': 'http://www.chnfund.com/list/CA2014032212333234517153%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr': ('h3.article-title',),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title': ('h2.title',),
                'pyq_date_author': {
                    'date': (re.compile(r'<span class="time" title="(.*?)">', re.S),),
                    'auth': ('.neirong-other .user', ),
                },
                'pyq_content': ('#articleShowBox div.content',)
            }
    },

]
