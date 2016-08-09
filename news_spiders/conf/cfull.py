# -*- coding: utf-8 -*-

""" Configs dict keys explain:
    `site`: string, website name, typ_sitename_other
    `urls`: list of dict obj, crawl all link in this site

    `block_attr`: tuple, including string, regex or tuple, Show all news link in one page, crawl it
        like as: ((css_selector, index), regex, ...)

    `remove_tags`: tuple, including string, regex or tuple, Remove some tags from crawled text
        like as: (css, regex, ....)
    `multi_page`: tuple, including css selector, Parser pagination
        like as: (css, regex, ....)

    `details`:  dict.   Crawl element tag:
        `pyq_title`: tuple od tuple, eg: ((css_selector, index), css, ...)
        `pyq_date_author` or `pyq_author_date`: dict, include `date` and `auth`, Note `date` and `auth` order
            like as:(css, regex, (css, sub_css, index), (css, None, index), ...)

    `pyq_content`: tuple, the same as `pyq_date_author`
        like as: (css, regex, (css, sub_css, index), (css, None, index), ...)

    `urls` about all links order:
        1: the news list page is order
        2: the news list page the first page is independent, and the order of the other page,
        3: the news list page is reverse, or the first page is independent and other pages is reverse order,
            set `first`, `suffix` and `reverse`is value
        4: Note that 'pyq_date_author', date and author maybe be required from multi relative tags
"""

import re

FULL_CONFIGS = [
    {
        'site': 'full_ifeng',
        'urls': [
            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/756/665/%s/dynlist.html', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/760/612/%s/dynlist.html', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/54/62/%s/dynlist.html', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/419/467/%s/dynlist.html', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/26/33/%s/dynlist.html', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/771/843/%s/dynlist.html', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.ifeng.com/cmppdyn/759/611/%s/dynlist.html', 'pages': 1,
                'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://tech.ifeng.com/%s', 'pages': 1,
                'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('h2', 'h3', '.list03', 'div.box01_hots.m01', 'div#morenews1'),
        'remove_tags': ('.picIntro', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#artical_topic', ),  # must this module
                'pyq_date_author':  {
                    'date': ('.ss01', ),
                    'auth': ('.ss03', ),
                },  # must this module
                'pyq_content':      ('#main_content', )  # must this module
            }
    },

    {
        'site': 'full_sina',
        'urls': [
            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/gncj/hgjj/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/cj4/cj_cyxw/%s.shtml',
                'pages': 1, 'first': 'index_%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/bx3/bxxw_xydt/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.sina.com.cn/money/insurance/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/bx3/bxgs_gsdt/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.sina.com.cn/money/bank/index.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/yh/gsdt/index_%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/zq1/ssgs/%s.shtml', 'pages': 1,
                'first': 'index_%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/gg/gsxw/%s.shtml', 'pages': 1,
                'first': 'index_%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://roll.finance.sina.com.cn/finance/cj4/cj_gsxw/%s.shtml',
                'pages': 1, 'first': 'index_%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://tech.sina.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('.list_009', '.blkTop', '.listS3', '[class="blk04"]', '.blk05',
                         '#impNews1', 'div[class="p"]'),
        'remove_tags': ('.img_descr', 'div[data-sudaclick="suda_1028_guba"]', '#sinashareto',
                        '.finance_app_zqtg',  '.hqimg_related', '.otherContent_01'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', '#main_title'),
                'pyq_date_author':  {
                    'date': ('.time-source', '#pub_date'),
                    'auth': ('.time-source', 'span[data-sudaclick="media_name"]', '#media_name')
                },
                'pyq_content':  (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S),
                                 '#artibody')
            }
    },

    {
        'site': 'full_sina_json',
        'urls': [
            {
                'page_url': 'http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1693&num=20&page=%s&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://feed.mix.sina.com.cn/api/roll/get?pageid=155&lid=1686&num=20&page=%s&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'json': {
            'data_key': 'result.data',
            'url_key': 'url'
        },
        'remove_tags': ('.img_descr', 'div[data-sudaclick="suda_1028_guba"]', '#sinashareto',
                        '.finance_app_zqtg',  '.otherContent_01'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', ),
                'pyq_date_author':  {
                    'date': ('.time-source', '#pub_date'),
                    'auth': ('.time-source', 'span[data-sudaclick="media_name"]', '#media_name')
                },
                'pyq_content':  (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S),
                                 '#artibody')
            }
    },

    {
        'site': 'full_qq',
        'urls': [
            {
                'page_url': 'http://finance.qq.com/c/hgjjllist_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.qq.com/c/gjcjlist_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://stock.qq.com/l/stock/shsgs/list20150423134920%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.qq.com/c/gsbdlist_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.qq.com/c/jrscllist_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.qq.com/c/gdyw_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.qq.com/l/insurance/bx_gs/index%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_%s', 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://stock.qq.com/l/stock/xingu/xgdt/list2015052081246%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_%s', 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://tech.qq.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_%s', 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/recodelist_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://bi.qq.com/c/bi2_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://tech.qq.com/c/tnw_%s.htm',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('.Q-tpWrap', '.newslist', 'a.pic'),
        'remove_tags': ('.pictext', '#invideocon', '#relInfo', '.hqimg_related', 'script', 'style'),
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
        'site': 'full_cnstock',
        'urls': [
            {
                'page_url': 'http://company.cnstock.com/lists/rdgs/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://company.cnstock.com/lists/gszx/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':   ('.main-list', ),
        'remove_tags':  ('u', '#contentPager'),
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
        'site': 'full_nbd',
        'urls': [
            {
                'page_url': 'http://www.nbd.com.cn/columns/35/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.nbd.com.cn/columns/23/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.nbd.com.cn/columns/44/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.nbd.com.cn/columns/39/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.nbd.com.cn/columns/38/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.nbd.com.cn/columns/45/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('p[class="h1"]', ),
        'remove_tags':  ('ul[class="right fr"]', '.pagination',  '.articleInfo', '.articleCopyright'),
        'details':
            {
                'pyq_title':        ('span[class="fl"]', ),
                'pyq_date_author':  {
                    'date': ('ul[class="left"]', ),
                    'auth': (('ul[class="left"]', 'span', 1), ),
                },
                'pyq_content':  ('.main-left-article', )
            }
    },

    {
        'site': 'full_yicai',
        'urls': [
            {
                'page_url': 'http://www.yicai.com/news/markets/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://www.yicai.com/news/finance/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://www.yicai.com/news/economy/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.yicai.com/news/well-being/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.yicai.com/news/world/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.yicai.com/news/business/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.yicai.com/news/technology/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.yicai.com/news/consumer/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

        ],
        'block_attr':   ('h3.f-ff1.f-fwn.f-fs22', ),
        'remove_tags':  ('p[style="text-align: center;"]', 'p[style="text-align:center"]'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_author_date':  {
                    'date': ('h2', ),
                    'auth': ('h2 i', ),
                },
                'pyq_content':  ('.m-text', )
            }
    },

    {
        'site': 'full_caixin',
        'urls': [
            {
                'page_url': 'http://companies.caixin.com/news/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.caixin.com/news/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://economy.caixin.com/news/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://companies.caixin.com/securities_news/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':   ('h4', ),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#Main_Content_Val', )
            }
    },

    {
        'site': 'full_wallstreetcn',
        'urls': [
            {
                'page_url': 'http://wallstreetcn.com/news?status=published&type=news&cid=17'
                            '&order=-created_at&limit=30&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('a[class="title"]', ),
        'details':
            {
                'pyq_title':        ('.article-title',),
                'pyq_date_author':  {
                    'date': ('.time', ),
                    'auth': ()
                },
                'pyq_content':      ('.article-content', )
            }
    },

    {
        'site': 'full_eeo',
        'urls': [
            {
                'page_url': 'http://www.eeo.com.cn/comment/commentsygc/commentsygccyzs/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.eeo.com.cn/industry/ssgs/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.eeo.com.cn/industry/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.eeo.com.cn/nation/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('.new_list', '.am_title', '.news_zxgx'),
        'remove_tags': ('#ContentPager', ),
        'details':
            {
                'pyq_title':        ('.wz_bt', ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#text_content', )
            }
    },

    {
        'site': 'full_stcn',
        'urls': [
            {
                'page_url': 'http://company.stcn.com/cjnews/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://company.stcn.com/gsxw/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://company.stcn.com/kj/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://company.stcn.com/qc/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://zt.stcn.com/list/gszt_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://company.stcn.com/dc/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'multi_page':   ('#pagination',),
        'block_attr':   ('#mainlist', ),
        'remove_tags':  ('.setFZ', '.om', 'script'),
        'details':
            {
                'pyq_title':        ('.txt_hd h1', '.intal_tit h2',),
                'pyq_date_author':  {
                    'date': ('.info', ),
                    'auth': ('.info', ),
                },
                'pyq_content':      ('#ctrlfscont', )
            }
    },

    {
        'site': 'full_thepaper',
        'urls': [
            {
                'page_url': 'http://www.thepaper.cn/load_index.jsp?nodeids=25434&topCids=&pageidx=%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.thepaper.cn/load_index.jsp?nodeids=25438&topCids=&pageidx=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.thepaper.cn/load_index.jsp?nodeids=25433&topCids=&pageidx=%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('h2', ),
        'remove_tags': ('span[style="color: rgb(128, 128, 128);"]', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('.news_title', ),
                'pyq_date_author':  {
                    'date': ('.news_about', ),
                    'auth': ('.news_path a:nth-child(2)', )
                },
                'pyq_content':      ('.news_txt', )
            }
    },

    {
        'site': 'full_ccstock',
        'urls': [
            {
                'page_url': 'http://www.ccstock.cn/gscy/gongsi/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.ccstock.cn/finance/hongguanjingji/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.ccstock.cn/finance/hangyedongtai/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.ccstock.cn/auto/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.ccstock.cn/finace/house/index_p%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.listMain', ),
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
        'site': 'full_cx368',
        'urls': [
            {
                'page_url': 'http://news.cx368.com/hots/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://news.cx368.com/china/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('.list', ),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('#newsinfo', ),
                    'auth': ('#newsinfo', ),
                },
                'pyq_content':  (('.content', None, 0), )
            }
    },

    {
        'site': 'full_jingji',
        'urls': [
            {
                'page_url': 'http://jingji.cntv.cn/jingji2013/gongsi/data/%s.json',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'remove_tags': ('em',),
        'json': {
            'data_key': 'rollData',
            'url_key': 'url'
        },
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_author_date':  {
                    'date': ('.info', ),
                    'auth': ('.info', ),
                },
                'pyq_content':  (re.compile(r'<!--repaste\.body\.begin-->(.*?)<!--repaste\.body\.end-->', re.S),)
            }
    },

    {
        'site': 'full_p5w',
        'urls': [
            {
                'page_url': 'http://www.p5w.net/news/gncj/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.p5w.net/news/cjxw/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.p5w.net/news/gjcj/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.p5w.net/news/hgzc/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.p5w.net/stock/news/gsxw/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.p5w.net/news/biz/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.p5w.net/news/cjxw/fdcy/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.p5w.net/stock/news/zqyw/%s.htm',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
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
        'site': 'full_p5w_ircs',
        'urls': [
            {
                'page_url': 'http://ircs.p5w.net/ircs/gszz/newsList.do?pageNo=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr': (re.compile(r'class="wz_text">.*?<a href="(?P<url>.*?)".*?'
                                  r'class="time_wz">(?P<date>.*?)</dt>', re.S),),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title': ('.bt_text',),
                'pyq_date_author': {
                    'date': (),
                    'auth': ()
                },
                'pyq_content': (re.compile(r'<td align="center">.*?</td>(.*?)</table>', re.S),)
            }
    },

    {
        'site': 'full_hexun',
        'urls': [
            {
                'page_url': 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?'
                            'id=100018985&s=30&cp=%s&priority=0&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?'
                            'id=100950568&s=30&cp=%s&priority=0&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix':None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?'
                            'id=108511812&s=30&cp=%s&priority=0&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?'
                            'id=100018983&s=30&cp=%s&priority=0&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?'
                            'id=100018982&s=30&cp=%s&priority=0&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?'
                            'id=108511056&s=30&cp=%s&priority=0&callback=',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'remove_tags': ('[style="text-align:right;font-size:12px"]', 'style', 'script'),
        "json": {
            "data_key": 'result',
            "url_key": "entityurl"
        },
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':  ('#artibody', )
            }
    },

    {
        'site': 'full_hexun_ot',
        'urls': [
            {
                'page_url': 'http://funds.hexun.com/hotnews/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://tech.hexun.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://trust.hexun.com/trust_company/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://insurance.hexun.com/bxgsxw/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://bank.hexun.com/yhlcyw/%shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.temp01', '#hiddList'),
        'remove_tags': ('[style="text-align:right;font-size:12px"]', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':  ('#artibody', )
            }
    },

    {
        'site': 'full_xinhua08',
        'urls': [
            {
                'page_url': 'http://news.xinhua08.com/hgjj/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://news.xinhua08.com/cyjj/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://app.xinhua08.com/prop.php?pid=56&cid=363&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://news.xinhua08.com/qyjj/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.newsinfo', 'section'),
        'remove_tags': ('font', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_author_date':  {
                    'date': ('[class="pull-left"]', ),
                    'auth': ('[class="pull-left"]', ),
                },
                'pyq_content':      ('#ctrlfscont', )
            }
    },

    {
        'site': 'full_qianzhan',
        'urls': [
            {
                'page_url': 'http://www.qianzhan.com/indynews/list/242-%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.qianzhan.com/indynews/list/150-%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.qianzhan.com/indynews/list/257-%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.qianzhan.com/indynews/list/258-%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.qianzhan.com/indynews/list/283-%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://t.qianzhan.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'multi_page':   ('.page',),
        'block_attr':   ('.pic', 'p.f22'),
        'remove_tags': ('p[style="padding-top:0px; font-style:italic;"]', 'i', 'div[class="mt30"]',
                        'style', 'script'),
        'details':
            {
                'pyq_title':        ('#h_title', 'h1.h1'),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', '.content_info'),
                    'auth': ('#source_baidu', '.content_info')
                },
                'pyq_content':  ('#div_content', '#content', 'div[class="art"]')
            }
    },

    {
        'site': 'full_takungpao',
        'urls': [
            {
                'page_url': 'http://finance.takungpao.com/gscy/cjyw/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/gscy/gsxw/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/hgjj/guoji/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/hgjj/quyu/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/financial/ssgs/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/financial/yaowen/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/tech/internet/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/tech/it/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/tech/mobile/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/tech/new-media/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.takungpao.com/gscy/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.a_time', 'list01'),
        'remove_tags':  ('p[style="text-align: center"]', ),
        'details':
            {
                'pyq_title':        ('.tpk_con_tle', ),
                'pyq_date_author':  {
                    'date': ('.article_info_l', ),
                    'auth': ('.article_info_l', ),
                },
                'pyq_content':      ('.tpk_text', )
            }
    },

    {
        'site': 'full_ce',
        'urls': [
            {
                'page_url': 'http://intl.ce.cn/hqcy/zxdt/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://intl.ce.cn/sjjj/qy/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.ce.cn/stock/gsgdbd/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.ce.cn/bank12/scroll/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.ce.cn/bank/dzyh/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.ce.cn/insurance1/scroll-news/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.ce.cn/insurance/ccbx/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.ce.cn/insurance/ylbx/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://tech.ce.cn/main/tech_corp/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.ce.cn/cysc/fdc/yw/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://district.ce.cn/newarea/jjdt/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.ce.cn/cysc/ny/gdxw/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('.lbcon', '.sec_left', '.font14', '.list', '.left'),
        'remove_tags': ('font', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#articleTitle',),
                'pyq_date_author':  {
                    'date': ('#articleTime', ),
                    'auth': ('#articleSource', )
                },
                'pyq_content':      ('#articleText', )
            }
    },

    {
        'site': 'full_china',
        'urls': [
            {
                'page_url': u'http://app.finance.china.com.cn/news/column.php?cname=国内经济&p=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': u'http://app.finance.china.com.cn/news/column.php?cname=国际经济&p=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': u'http://app.finance.china.com.cn/news/column.php?cname=公司新闻&p=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': u'http://app.finance.china.com.cn/news/column.php?cname=上市公司&p=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': u'http://app.finance.china.com.cn/news/column.php?cname=产经要闻&p=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': u'http://app.finance.china.com.cn/news/live.php?channel=产经&p=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': u'http://app.tech.china.com.cn/news/column.php?cname=互联网&p=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://tech.china.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr':   ('.news_list', 'h3.hsTit3'),
        'remove_tags': ('p[align=center]', 'div[class="fr bianj"]'),
        'details':
            {
                'pyq_title':        (('h1', 2), 'h1.toph1'),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', 'span.fl.time2'),
                    'auth': ('#source_baidu', 'span.fl.time2')
                },
                'pyq_content':  ('#content', 'div#fontzoom')
            }
    },

    {
        'site': 'full_huagu',
        'urls': [
            {
                'page_url': 'http://finance.huagu.com/gn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.huagu.com/gj/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.huagu.com/cjyw/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.huagu.com/hg/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://stock.huagu.com/gegu/gsxw/%s',
                'pages': 1, 'first': '', 'suffix': None, 'reverse': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.huagu.com/jr/%s',
                'pages': 1, 'first': '', 'suffix': None, 'reverse': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':   ('.ul-news-list', ),
        'remove_tags': ('.page', ),
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
        'site': 'full_2258',
        'urls': [
            {
                'page_url': 'http://www.2258.com/news/hgjj/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.2258.com/news/zjyw/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.2258.com/industry/cyjj/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.2258.com/domestic/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.2258.com/company/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.2258.com/company/gsxw/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'multi_page': ('.pages',),
        'block_attr':   ('h4', ),
        'details':
            {
                'pyq_title':        ('.pagetit',),
                'pyq_date_author':  {
                    'date': ('.info', ),
                    'auth': ('.info_ly',)
                },
                'pyq_content':      ('#content_font', )
            }
    },

    {
        'site': 'full_591hx',
        'urls': [
            {
                'page_url': 'http://finance.591hx.com/lista/hgjj%s.shtml',
                'pages': 1, 'suffix': None, 'cate': u'宏观新闻', 'reverse': None, 'first': '',
            },

            {
                'page_url': 'http://finance.591hx.com/lista/gjlc%s.shtml',
                'pages': 1, 'suffix': None, 'cate': u'宏观新闻', 'reverse': None,  'first': '',
            },

            {
                'page_url': 'http://finance.591hx.com/lista/gs%s.shtml',
                'pages': 1, 'suffix': None, 'cate': u'公司新闻', 'reverse': None, 'first': '',
            },

            {
                'page_url': 'http://stock.591hx.com/list/ssgs%s.shtml',
                'pages': 2, 'suffix': None, 'cate': u'公司新闻', 'reverse': None, 'first': '',
            },

            {
                'page_url': 'http://finance.591hx.com/lista/qyjj%s.shtml',
                'pages': 1, 'suffix': None, 'cate': u'宏观新闻', 'reverse': None, 'first': '',
            },
        ],
        'block_attr':   ('.newList', ),
        'remove_tags': ('script', 'select'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('.info', ),
                    'auth': ('.info', ),
                },
                'pyq_content':      ('#newsCon', )
            }
    },

    {
        'site': 'full_cs',
        'urls': [
            {
                'page_url': 'http://www.cs.com.cn/xwzx/hg/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.cs.com.cn/xwzx/cj/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.cs.com.cn/ssgs/gsxw/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.cs.com.cn/xwzx/zq/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.cs.com.cn/xwzx/jr/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.cs.com.cn/ssgs/fcgs/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.cs.com.cn/ssgs/kj/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.column-box', ),
        'remove_tags': ('p[style="text-align: center"]', 'style', 'script'),
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

    {
        'site': 'full_yingfu001',
        'urls': [
            {
                'page_url': 'http://finance.yingfu001.com/gnjj/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.yingfu001.com/corporation/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.yingfu001.com/global/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://stock.yingfu001.com/bkzx/index_%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.title', ),
        'remove_tags': ('p[style="text-align: center;"]', ),
        'details':
            {
                'pyq_title':        ('.title', ),
                'pyq_date_author':  {
                    'date': ('.title2l', ),
                    'auth': ('.title2l', ),
                },
                'pyq_content':      ('.txt', )
            }
    },

    {
        'site': 'full_capitalweek',
        'urls': [
            {
                'page_url': 'http://www.capitalweek.com.cn/small_article_list/2%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.capitalweek.com.cn/small_article_list/4%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.view-content', ),
        'details':
            {
                'pyq_title':        ('#art_page_title_fx', ),
                'pyq_date_author':  {
                    'date': ('.views-field-created', ),
                    'auth': ('.views-field-created', ),
                },
                'pyq_content':      ('.field-items', )
            }
    },

    {
        'site': 'full_chinanews',
        'urls': [
            {
                'page_url': 'http://channel.chinanews.com/u/finance/gs%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://channel.chinanews.com/cns/cl/cj-chjcy%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://channel.chinanews.com/cns/cl/cj-hgds%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://channel.chinanews.com/u/finance/yw.shtml?pager=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://channel.chinanews.com/u/jryj.shtml?pager=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.color065590', '.content_list'),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('.left_zw', )
            }
    },

    {
        'site': 'full_jrj',
        'urls': [
            {
                'page_url': 'http://finance.jrj.com.cn/list/guoneicj%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.jrj.com.cn/list/guojicj%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.jrj.com.cn/list/industrynews%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.jrj.com.cn/biz/biz_index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.jrj.com.cn/tech/tech_index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.jrj.com.cn/list/companynews%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.list2', ),
        'remove_tags': ('font', 'style', 'script'),
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
        'site': 'full_eastmoney',
        'urls': [
            {
                'page_url': 'http://finance.eastmoney.com/news/ccjxw_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.eastmoney.com/news/cssgs_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.eastmoney.com/yaowen_cgnjj_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.eastmoney.com/yaowen_cgjjj_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://stock.eastmoney.com/news/czggng_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://bond.eastmoney.com/news/czqxw_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://bank.eastmoney.com/news/czzyh_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://fund.eastmoney.com/news/cjjyw_%s.html', 'pages': 2, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.eastmoney.com/yaowen%s.html', 'pages': 1, 'first': '',
                'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://finance.eastmoney.com/news/cgsxw_%s.html', 'pages': 1, 'first': '%s',
                'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'multi_page':   ('.Page',),
        'block_attr': ('.listBox', '.title'),
        'remove_tags': ('.c_review', ),
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
        'site': 'full_cnfol',
        'urls': [
            {
                'page_url': 'http://news.cnfol.com/guoneicaijing/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://news.cnfol.com/guojicaijing/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://news.cnfol.com/chanyejingji/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://news.cnfol.com/zhengquanyaowen/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'multi_page': ('#page',),
        'block_attr': ('.NewsLstItem', ),
        'remove_tags': ('.text-pic-tt', 'style', 'script'),
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
        'site': 'full_stockstart',
        'urls': [
            {
                'page_url': 'http://finance.stockstar.com/list/955%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.stockstar.com/list/2863%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.stockstar.com/list/2921%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.stockstar.com/list/1221%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://bank.stockstar.com/list/1743%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://stock.stockstar.com/list/10%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://fund.stockstar.com/list/1293%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr': ('.list-line', ),
        'remove_tags': ('[class="tags"]', ),
        'details':
            {
                'pyq_title':        ('h1',),
                'oyq_date_author': {
                    'date': ('#pubtime_baidu', ),
                    'auth': ("#source_baidu", )
                },
                'pyq_content':      ('.article', )
            }
    },

    {
        'site': 'full_163',
        'urls': [
            {
                'page_url': 'http://money.163.com/special/00252G50/macro%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix':None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://money.163.com/special/g/00251LR5/gsxw%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://money.163.com/stock/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '', 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://money.163.com/special/00251LJV/hyyj%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://money.163.com/chanjing/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://tech.163.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'block_attr': ('.col_l', '.head', '.news_hot_list', '.fn_area_left', 'div.hb_detail'),
        'remove_tags': (re.compile(r'<!--biaoqian.*?>.*?<!--biaoqian.*?>', re.S),
                        'div[class="ep-source cDGray"]', '.nph_photo', '.nph_photo_ctrl',
                        '.nvt_vote_2', '.demoBox', '.hidden', 'script', 'style'),
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
        'site': 'full_10jqka',
        'urls': [
            {
                'page_url': 'http://news.10jqka.com.cn/cjkx_list/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://stock.10jqka.com.cn/companynews_list/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://news.10jqka.com.cn/cjzx_list/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://news.10jqka.com.cn/guojicj_list/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://news.10jqka.com.cn/today_list/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://stock.10jqka.com.cn/companynews_list/%s.shtml',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://stock.10jqka.com.cn/stocknews_list/%s.shtml',
                'pages':12, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('h2', 'span.arc-title'),
        'remove_tags':  ('#editor_baidu', 'a.backweb', 'script', 'style'),
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
        'site': 'full_21cn',
        'urls': [
            {
                'page_url': 'http://finance.21cn.com/news/macro/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.21cn.com/news/industry/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.21cn.com/stock/ssgs/list%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':       ('h3', ),
        'remove_tags':      ('script', 'style'),
        'details':
            {
                'pyq_title':        ('[class="title"]', ),
                'pyq_date_author': {
                    'date': ('.pubTime', ),
                    'auth': ('a[rel="nofollow"]', )
                },
                'pyq_content':      ('#article_text', )
            }
    },

    {
        'site': 'full_people',
        'urls': [
            {
                'page_url': 'http://finance.people.com.cn/GB/153179/153476/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.people.com.cn/GB/153179/153475/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://finance.people.com.cn/GB/153179/153180/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://finance.people.com.cn/stock/GB/68055/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://energy.people.com.cn/GB/71890/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://energy.people.com.cn/GB/71895/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://it.people.com.cn/GB/243510/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://auto.people.com.cn/GB/14555/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':       ('.ej_left', '.ej_list', '[class="d2_2 clear"]'),
        'remove_tags': ('.pictext', '.otitle', '.edit'),
        'details':
            {
                'pyq_title':        ('#p_title', ),
                'pyq_date_author': {
                    'date': ('#p_publishtime', ),
                    'auth': ("#p_origin", )
                },
                'pyq_content':      ('#p_content', )
            },
    },

    {
        'site': 'full_ceh',
        'urls': [
            {
                'page_url': 'http://www.ceh.com.cn/cjpd/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

        ],
        'block_attr': ('.bg_color_blue', ),
        'details':
            {
                'pyq_title':        (".title_content", ),
                'pyq_date_author':   {
                    'date': ('.date_content', ),
                    'auth': ('.date_content', ),
                },
                'pyq_content':      (('.content3', None, 1), ),
            }
    },

    {
        'site': 'full_sohu',
        'urls': [
            {
                'page_url': 'http://business.sohu.com/guoneixinwen%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://business.sohu.com/chanjing%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://business.sohu.com/gongsi%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://business.sohu.com/FinancialNews/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://business.sohu.com/FinancialNews/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            # {
            #     'page_url': 'http://it.sohu.com/internet%s.shtml',
            #     'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            # },
        ],
        'block_attr': ('.lc', '.content-title'),
        'remove_tags': ('span[style="font-size: 12px;"]', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author': {
                    'date': ('#pubtime_baidu', ),
                    'auth': ("#media_span", 'span[class="writer"]')
                },
                'pyq_content':      ('[itemprop="articleBody"]', )
            }
    },

    {
        'site': 'full_southcn',
        'urls': [
            {
                'page_url': 'http://finance.southcn.com/ssgs/node_189041.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.southcn.com/f/node_165971.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

        ],
        'block_attr':       ('.list',),
        'remove_tags':      ('.pictext', ),
        'details':
            {
                'pyq_title':        ('#article_title',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#content',)
            }
    },

    {
        'site': 'full_eastday',
        'urls': [
            {
                'page_url': 'http://finance.eastday.com//Business/rdjj/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':       ('[class="fl"]',),
        'remove_tags':      ('.pictext', ),
        'details':
            {
                'pyq_title':        ('#biaoti',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('.time a', )
                },
                'pyq_content':      ('#zw1',)
            }
    },

    {
        'site': 'full_gdcenn',
        'urls': [
            {
                'page_url': 'http://www.gdcenn.cn/news_list.asp?page=%s&ClassID=8',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':       ('.qhnr', '.uuggg'),
        'remove_tags':      ('#commentNum', 'p[align="center"]'),
        'details':
            {
                'pyq_title':        ('.znn',),
                'pyq_date_author':  {
                    'date': ('.znnxx', ),
                    'auth': ('.znnxx', ),
                },
                'pyq_content':      ('#articlecon',)
            }
    },

    {
        'site': 'full_people_cc',
        'urls': [
            {
                'page_url': 'http://ccnews.people.com.cn/GB/142057/index%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':       ('.hdNews strong', ),
        'details':
            {
                'pyq_title':        (('#p_title', 0), ),
                'pyq_date_author':  {
                    'date': ('#p_publishtime',),
                    'auth': ('#p_origin',)
                },
                'pyq_content':      ('#p_content',)
            }
    },

    {
        'site': 'full_xinhuanet',
        'urls': [
            {
                'page_url': 'http://www.news.cn/energy/index%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.news.cn/fortune/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.news.cn/auto/index%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.news.cn/tech/index%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'multi_page':   ('#div_currpage',),
        'block_attr': ('.impNews', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('#title', ),
                'pyq_date_author': {
                    'date': ('.time',),
                    'auth': ('#source',),
                },
                'pyq_content':      ('.article',)
            }
    },

    {
        'site': 'full_caijing',
        'urls': [
            {
                'page_url': 'http://economy.caijing.com.cn/economynews/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://industry.caijing.com.cn/industrianews/%s.shtml',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://stock.caijing.com.cn/stocknews/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://stock.caijing.com.cn/companystock/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://tech.caijing.com.cn/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://estate.caijing.com.cn/estatenews/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr': ('.list', '.list_title'),
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
        'site': 'full_fx168',
        'urls': [
            {
                'page_url': 'http://news.fx168.com/top/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr': ('.yjl_fx168_focus_TodayNews', '.yjl_fx168_news_listTitle'),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_author_date': {
                    'date': ('.shijian',),
                    'auth': ('.laiyuan', ),
                },
                'pyq_content':      ('.yjl_fx168_article_zhengwen', )
            }
    },

    {
        'site': 'full_cet',
        'urls': [
            {
                'page_url': 'http://www.cet.com.cn/cjpd/hg/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('.font_05', ),
        'details':
            {
                'pyq_title':        ('h2[align="center"]', ),
                'pyq_author_date':  {
                    'date': ('.time', ),
                    'auth': ('.time', ),
                },
                'pyq_content':      ('.article_content', )
            }
    },

    {
        'site': 'full_17ok',
        'urls': [
            {
                'page_url': 'http://stock.17ok.com/list.php?id=808%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://finance.17ok.com/list.php?id=7%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u' 行业新闻'
            },

            {
                'page_url':  'http://finance.17ok.com/list.php?id=4%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u' 宏观新闻'
            },

            {
                'page_url':  'http://finance.17ok.com/list.php?id=5%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u' 宏观新闻'
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
        'site': 'full_glinfo',
        'urls': [
            {
                'page_url': 'http://www.glinfo.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://info.glinfo.com/article/p-319------0-0-0-----%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://qh.glinfo.com/article/p-317-------------%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('ul.nlist', ('.blk12', 0)),
        'remove_tags': ('[style="color:#F00;"]',),
        'details':
            {
                'pyq_title':        ('#articleContent h1', ),
                'pyq_date_author':  {
                    'date': ('.info', ),
                    'auth': ('.info', ),
                },
                'pyq_content':      ('#text', )
            }
    },

    {
        'site': 'full_21jingji',
        'urls': [
            {
                'page_url': 'http://www.21jingji.com/channel/money/shangshigongsi/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':   ('.titles', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('.the_title', ),
                'pyq_author_date':  {
                    'date': ('.the_title2', ),
                    'auth': ('.the_title2', )
                },
                'pyq_content':  ('#Article', )
            }
    },

    {
        'site': 'full_opsteel',
        'urls': [
            {
                'page_url': 'http://www.opsteel.cn/news/ynsd%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.opsteel.cn/news/fcjj%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.opsteel.cn/news/qcjd%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.opsteel.cn/news/cbjx%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.newsmainlist', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('#article h1', ),
                'pyq_date_author':  {
                    'date': ('.ref-de-publish', ),
                    'auth': ()
                },
                'pyq_content':  ('#articlebody', )
            }
    },

    {
        'site': 'full_eworldship',
        'urls': [
            {
                'page_url': 'http://www.eworldship.com/shipbuilding%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.eworldship.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('#layout-news', '[class="m-list list-main pb12"]', ('div.news-hot.box', 0),
                         '#tabPanel0', '#tabPanel2 ', '#tabPanel1'),
        'remove_tags': ('.news_xgyd', '[style="text-align: center;"]', 'style', 'script'),
        'multi_page':   ('#pages', ),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.ss01', ),
                    'auth': ('.ss03', )
                },
                'pyq_content':  (('[class="content"]', None, 1), )
            }
    },

    {
        'site': 'full_cnforex',
        'urls': [
            {
                'page_url': 'http://www.cnforex.com/news/hstt/default.aspx?shwqg=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('.first', ),
        'remove_tags': ('#exe_ding', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('.h1Title', ),
                'pyq_date_author':  {
                    'date': ('.spanShowTime', ),
                    'auth': ()
                },
                'pyq_content':  ('.divContent', )
            }
    },

    {
        'site': 'full_jiemian',
        'urls': [
            {
                'page_url': 'http://www.jiemian.com/lists/20.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('#load-list h3',),
        'remove_tags': ('.article-source', ),
        'details':
            {
                'pyq_title':        ('.article-header h1', ),
                'pyq_author_date':  {
                    'date': ('.article-info .date', ),
                    'auth': ()
                },
                'pyq_content':  ('.article-content', )
            }
    },

    {
        'site': 'full_cnenbd',
        'urls': [
            {
                'page_url': 'http://www.cnenbd.com/Article/ShowClass.asp?ClassID=28%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':   ('td[width="699"]',),
        'remove_tags': ('.article-source', ),
        'details':
            {
                'pyq_title':        ('td[class="511xxtitle"]', ),
                'pyq_author_date':  {
                    'date': (('.main_Articlets', None, 3), ),
                    'auth': (('.main_Articlets', None, 1), )
                },
                'pyq_content':  ('div[class="511xxcontent"]', )
            }
    },

    {
        'site': 'full_brandcn',
        'urls': [
            {
                'page_url': 'http://news.brandcn.com/pinpaixinwen/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },
        ],
        'block_attr':   (re.compile(r'<li class="li01">.*?<h3>.*?'
                                    r'<a href="(?P<url>.*?)".*?>.*?</a>.*?'
                                    r'<span>(?P<date>\d{4}.*?)</span>.*?</li>', re.S),
                         ),
        'remove_tags': ('.tag', ),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_author_date':  {
                    'date': (),
                    'auth': ()
                },
                'pyq_content':  ('#vcontent', )
            }
    },

    {
        'site': 'full_cnmn',
        'urls': [
            {
                'page_url': 'http://www.cnmn.com.cn/ShowNewsList.aspx?id=43&pageindex=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'block_attr':   ('h4', ),
        'remove_tags': (),
        'details':
            {
                'pyq_title':        (('h4', 0), ),
                'pyq_author_date':  {
                    'date': ('.time', ),
                    'auth': ('a[rel="tag"]', )
                },
                'pyq_content':  ('#txtcont', )
            }
    },

    {
        'site': 'full_zaobao',
        'urls': [
            {
                'page_url': 'http://www.zaobao.com/finance/china%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://www.zaobao.com/finance/world%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'宏观新闻'
            },
        ],
        'block_attr':   ('#l_title', ),
        'remove_tags': ('.article-below-container', ),
        'details':
            {
                'pyq_title':        ('[itemprop="headline"]', ),
                'pyq_author_date':  {
                    'date': ('.time', ),
                    'auth': ()
                },
                'pyq_content':  ('.a_body', )
            }
    },

    {
        'site': 'full_haowaicaijing',
        'urls': [
            {
                'page_url': 'http://www.haowaicaijing.com/html/ssgs/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': '%s', 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://www.haowaicaijing.com/html/hlwjr/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': '%s', 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.haowaicaijing.com/html/jijing/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': '%s', 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://www.haowaicaijing.com/html/qiche/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': '%s', 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://www.haowaicaijing.com/html/yiyao/%s.html',
                'pages': 1, 'first': 'index', 'reverse': None, 'suffix': '%s', 'cate': u'行业新闻'
            },
        ],
        'block_attr': ('div.bulletin', 'div.topnews'),
        'remove_tags': ('ul#share', 'p[style="text-align:center;text-indent:0;"]'),
        'details':
            {
                'pyq_title': (('div.article h3', 0),),
                'pyq_date_author': {
                    'date': ('div.article div.sj',),
                    'auth': (
                        re.compile(u'<div class="sj">.*?来源[：:]<a.*?>(.*?)</a>', re.S),
                        re.compile(u'<div class="sj">.*?来源[：:](.*?)</span>', re.S),
                    ),
                },
                'pyq_content': ('#Article',)
            }
    },

    {
        'site': 'full_china_economy',
        'urls': [
            {
                'page_url': 'http://economy.china.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://economy.china.com/domestic/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_%s', 'cate': u'宏观新闻'
            },

            {
                'page_url': 'http://economy.china.com/industrial/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': '_%s', 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://ec.china.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://ec.china.com/ecyd/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },
        ],
        'multi_page': ('div#chan_multipageNumN', ),
        'block_attr':   ('h3[class="item-tit"]', ),
        # 'remove_tags': ('div.chan_newsInfo_link', 'span.chan_newsInfo_comment'),
        'details':
            {
                'pyq_title':        ('#chan_newsTitle', ),
                'pyq_date_author':  {
                    'date': ('div#chan_newsInfo', ),
                    'auth': ('div#chan_newsInfo', )
                },
                'pyq_content':  ('div#chan_newsDetail', )
            }
    },

    {
        'site': 'full_hongzhoukan',
        'urls': [
            {
                'page_url': 'http://news.hongzhoukan.com/article_list.php?id=394&page_id=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'公司新闻'
            },

            {
                'page_url': 'http://news.hongzhoukan.com/article_list.php?id=310&page_id=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'行业新闻'
            },

            {
                'page_url': 'http://news.hongzhoukan.com/article_list.php?id=336&page_id=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://news.hongzhoukan.com/article_list.php?id=331&page_id=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'股评新闻'
            },

            {
                'page_url': 'http://news.hongzhoukan.com/article_list.php?id=326&page_id=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },

            {
                'page_url': 'http://news.hongzhoukan.com/article_list.php?id=328&page_id=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'基金新闻'
            },
        ],
        'block_attr': ('div[class="list_one"] ul', ),
        'remove_tags': ('p[class="sp"]',),
        'details':
            {
                'pyq_title': ('div[class="article"] h1', ('h1[style="font-weight:bolder"]', 0)),
                'pyq_date_author': {
                    'date': (('div[class="article"] h2', 'span', 0),
                             re.compile(r'<div class="newsc_inf".*>(.*?)%s' % u'来源', re.S)),

                    'auth': (('div[class="article"] h2', 'span', 1),
                             re.compile(r'%s[%s](.*?)\s+' % (u'来源', u':：'), re.S))
                },
                'pyq_content': ('div[class="article"] p', 'div.newsc_dcontent')
            }
    },

    {
        'site': 'full_36kr',
        'urls': [
            {
                'page_url': 'http://36kr.com/api/info-flow/main_site/posts?column_id=&b_id=5050227&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=67&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=68&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=23&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=69&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=70&b_id=&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },

            {
                'page_url': 'http://36kr.com/api/post?column_id=71&b_id=5046510&per_page=100%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'科技新闻'
            },
        ],
        'json': {
            'data_key': 'data.items',
            'url_key': 'id',
            'date_key': 'published_at',
            'join_key': 'http://36kr.com/p/{url}.html'
        },
        'is_script': True,
        'remove_tags': (),
        'details':
            {
                'pyq_title':        (re.compile(r'"title":"(.*?)","', re.S), ),
                'pyq_date_author':  {
                    'date': (),
                    'auth': ()
                },
                'pyq_content':  (re.compile(r'"content":"(.*?)","', re.S), )
            }
    },

    {
        'site': 'full_jd',
        'urls': [
            {
                'page_url': 'https://gupiao.jd.com/index/newsList.html?pageSize=10&pageNum=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'京东新闻'
            },

            {
                'page_url': 'https://gupiao.jd.com/usNews/ulist.html?pageSize=10&pageNum=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': u'京东美股'
            },
        ],
        'block_attr': ('a.c-li-title', ),
        'remove_tags': (),
        'details':
            {
                'pyq_title': ('h2[class="title details-title"]',),
                'pyq_date_author': {
                    'date': ('div[class="typical details-typical font-gray"]',),
                    'auth': ('div[class="typical details-typical font-gray"]', ),
                },
                'pyq_content': ('div[class="article"]',)
            }
    },

]
