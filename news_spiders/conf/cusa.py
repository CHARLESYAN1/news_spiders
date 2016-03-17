# -*- coding: utf-8 -*-

# Description category about USA Stock News
# 美股个股: us_gg
# 美股宏观: us_hg
# 美股股市: us_gs
# 美股行业: us_hy

import re

USA_CONFIGS = [
    {
        'site': 'usa_sina',
        'urls': [
            {
                'page_url': 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?'
                            'col=49&spec=&type=&ch=03&k=&offset_page=0&offset_num=0&num=60&asc=&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'json': {
            'url_key': 'url',
            'data_key': 'list'
        },
        'remove_tags': ('.img_descr', '.otherContent_01', '.xb_new_finance_app', '.hqimg_related', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', ),
                'pyq_date_author':  {
                    'date': ('#pub_date', '.titer'),
                    'auth': ('#media_name', '.source', )
                },
                'pyq_content':      ('#artibody', )
            }
    },

    {
        'site': 'usa_qq',
        'urls': [
            {
                'page_url': 'http://stock.qq.com/l/usstock/huanqiucaijing/list20150520144736%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://stock.qq.com/l/usstock/xwzx/list20150520145033%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://stock.qq.com/l/usstock/usgdyw/list20150520144638%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://stock.qq.com/l/usstock/energy_option/list201506181117%s.htm',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },
        ],
        'block_attr': ('h3', 'div.mod.newslist'),
        'remove_tags': ('.pictext', '#invideocon', '#relInfo', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.pubTime', ),
                    'auth': ('.where', )
                },
                'pyq_content':      ('#Cnt-Main-Article-QQ', )
            }
    },

    {
        'site': 'usa_hexun',
        'urls': [
            {
                'page_url': 'http://stock.hexun.com/mggi/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://stock.hexun.com/gainiangu/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://stock.hexun.com/usdongtai/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('.temp01', ),
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
        'site': 'usa_sohu',
        'urls': [
            {
                'page_url':   'http://stock.sohu.com/us/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
                 ],
        'block_attr':   ('.list', ),
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
        'site': 'usa_163',
        'urls': [
            {
                'page_url':   'http://money.163.com/special/00252U8L/mgdt%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url':   'http://money.163.com/special/00252U8L/zggng_mg%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url':   'http://money.163.com/usstock%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('.item_top', ('.colM .content', 0), ('.colM .content', 1), ('.colM .content', 2)),
        'remove_tags': (re.compile(r'<!--biaoqian.*?>.*?<!--biaoqian.*?>', re.S),
                        'div[class="ep-source cDGray"]', '.nph_photo', '.nph_photo_ctrl',
                        '.nvt_vote_2', '.demoBox', '.hidden'),
        'details':
            {
                'pyq_title':        ('#h1title',),
                'pyq_date_author': {
                    'date': ('.ep-time-soure', ),
                    'auth': ('.ep-time-soure', ),
                },
                'pyq_content':      ('div#endText', )
            },
    },

    {
        'site': 'usa_jrj',
        'urls': [
            {
                'page_url': 'http://usstock.jrj.com.cn/list/mgyw%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://usstock.jrj.com.cn/list/mggd%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://usstock.jrj.com.cn/list/yjfx%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://usstock.jrj.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://usstock.jrj.com.cn/list/zggng%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },
        ],
        'block_attr':   ('.ull', 'div.text-m1', 'ul.line'),
        'remove_tags': ('[color="#800000"]', '[style="COLOR: #800000"]', 'style', 'script'),
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
        'site': 'usa_21so',
        'urls': [
            {
                'page_url': 'http://stocks.21so.com/meigu/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
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
        'site': 'usa_ifeng',
        'urls': [
            {
                'page_url': 'http://tech.ifeng.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/801/1/list.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/803/1/list.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/806/1/list.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/11516/1/list.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://tech.ifeng.com/listpage/11493/1/list.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },
        ],
        'block_attr':   ('.hotNews', '.t_css'),
        'remove_tags':  ('.picIntro', ),
        'details':
            {
                'pyq_title':        ('#artical_topic',),
                'pyq_date_author':  {
                    'date': ('.ss01', ),
                    'auth': ('.ss03', )
                },
                'pyq_content':      ('#main_content', )
            }
    },

    {
        'site': 'usa_cnetnews',
        'urls': [
            {
                'page_url': 'http://www.cnetnews.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.cnetnews.com.cn/files/list-0-6-0-0-1-0.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            {
                'page_url': 'http://www.cnetnews.com.cn/files/list-0-0-322824-0-1.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            {
                'page_url': 'http://www.cnetnews.com.cn/biz.shtml%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },
        ],
        'block_attr':   (re.compile(r'<div class="qu_times">(?P<date>.*?)</div>.*?'
                                    r'<div class="qu_ims"><a href="(?P<url>.*?)"', re.S), ),
        'remove_tags':  (),
        'details':
            {
                'pyq_title':        ('.foucs_title', '.qu_ti', '.qu_wenzhang_tit_row h1'),
                'pyq_date_author':  {
                    'date': (),
                    'auth': (re.compile(r'%s' % u'<div class="qu_zuo">.*?来源(.*?)\s', re.S),
                             re.compile(r'%s' % u'<p class="qu_zuc">.*?来源(.*?)\s', re.S),
                             re.compile(r'%s' % u'<span class="qu_laiyuan">.*?来源(.*?)</span>', re.S),
                             )
                },
                'pyq_content':      ('.qu_ocn', '.qu_content_div', '.qu_wenzhang_con_div')
            }
    },

    {
        'site': 'usa_ftchinese',
        'urls': [
            {
                'page_url': 'http://www.ftchinese.com/channel/usa.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/globaleconomy.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/technology.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/auto.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/energy.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/industrials.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/airline.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/pharma.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },
        ],
        'block_attr':   ('.coverlink', 'a.thl', '#column1'),
        'multi_page':   ('.pagination',),
        'details':
            {
                'pyq_title':        ('#topictitle',),
                'pyq_date_author':  {
                    'date': ('.storytime',),
                    'auth': ()
                },
                'pyq_content':      ('.content-text',)
            }
    },

    {
        'site': 'usa_finet',
        'urls': [
            {
                'page_url': 'http://www.finet.com.cn/hwstocks/meiguogushi/list_31_%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },
        ],
        'block_attr':   ('.s_n_m', ),
        'remove_tags':  ('p[finetTip="finetNet"]', ),
        'details':
            {
                'pyq_title':        ('.news_tit_big', ),
                'pyq_date_author':  {
                    'date': ('.news_from_left', ),
                    'auth': ('.news_from_left', )
                },
                'pyq_content':      ('#fdfx', )
            }
    },

    {
        'site': 'usa_chineseworldnet',
        'urls': [
            {
                'page_url': 'http://www.chineseworldnet.com/na/stock/financeNewsGroup/financial_news%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.chineseworldnet.com/na/stock/financeNewsGroup/pr_news_na%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.chineseworldnet.com/na/stock/financeNewsGroup/quote123_news%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.chineseworldnet.com/na/stock/financeNewsGroup/company_news%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },
        ],
        'block_attr':   ('#content-area', ),
        'remove_tags':  (),
        'details':
            {
                'pyq_title':        ('h2.title', ),
                'pyq_date_author':  {
                    'date': ('.cwnfn-last-update', ),
                    'auth': ()
                },
                'pyq_content':      (('[class="content"]', None, 1), )
            }
    },

    {
        'site': 'usa_takungpao',
        'urls': [
            {
                'page_url': 'http://finance.takungpao.com/tech/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            {
                'page_url': 'http://finance.takungpao.com/tech/kjgd/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            # Temporary ignore
            # {
            #     'page_url': 'http://finance.takungpao.com/hkstock/qqgs/%s',
            #     'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            # },
        ],
        'block_attr':   ('.a_time', 'list01', 'div.HB_1'),
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
        'site': 'usa_yzforex',
        'urls': [
            {
                'page_url': 'http://www.yzforex.com/index.php?m=content&c=index&a=lists&catid=22%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('.m-list', ),
        'remove_tags':  ('#comment', '#hits'),
        'details':
            {
                'pyq_title':        (re.compile(r'<h1.*?>(.*?)<br', re.S),),
                'pyq_date_author':  {
                    'date': ('h1 span',),
                    'auth': ('h1 span', )
                },
                'pyq_content':      ('.content',)
            }
    },

    {
        'site': 'usa_forbeschina',
        'urls': [
            {
                'page_url': 'http://www.forbeschina.com/investment/stock/0/page/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },
        ],
        'block_attr':   ('.buss_left_left_title', ),
        'remove_tags':  ('.rich_card', ),
        'details':
            {
                'pyq_title':        ('#article_title',),
                'pyq_date_author':  {
                    'date': ('h6[class="p_message"]',),
                    'auth': ()
                },
                'pyq_content':      ('.detail',)
            }
    },

    {
        'site': 'usa_wallstreetcn',
        'urls': [
            {
                'page_url': 'http://wallstreetcn.com/news?cid=16%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('a[class="title"]', ),
        'details':
            {
                'pyq_title':        ('.article-title',),
                'pyq_date_author':  {
                    'date': ('.time', ),
                    'auth': ('.time', ),
                },
                'pyq_content':      ('.article-content', )
            }
    },

    {
        'site': 'usa_meigu18',
        'urls': [
            {
                'page_url': 'http://www.meigu18.com/zggng/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.meigu18.com/mgxw/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.meigu18.com/cbgg/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://www.meigu18.com/rgdp/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gs'
            },

            {
                'page_url': 'http://www.meigu18.com/dpfx/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gs'
            },

            {
                'page_url': 'http://www.meigu18.com/scyw/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://www.meigu18.com/jrsd/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://www.meigu18.com/mjgd/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('ul.newsList', ),
        'details':
            {
                'pyq_title':        ('.newsTitle',),
                'pyq_date_author':  {
                    'date': ('.newsInfo', ),
                    'auth': (),
                },
                'pyq_content':      ('.newsDetail', )
            }
    },

    {
        'site': 'usa_10jqka',
        'urls': [
            {
                'page_url': 'http://stock.10jqka.com.cn/usstock/mggsxw_list/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://stock.10jqka.com.cn/usstock/zggxw_list/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://stock.10jqka.com.cn/usstock/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('h2', 'span.arc-title', 'h4.news-tit'),
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
        'site': 'usa_yahoo',
        'urls': [
            {
                'page_url': 'https://hk.finance.yahoo.com/news/provider-afp/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('li[class="thumb clearfix"]', ),
        'is_script': False,
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
        'site': 'usa_bwchinese',
        'urls': [
            {
                'page_url': 'http://www.bwchinese.com/channel/usa.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('div.con_01_01left', ),
        'multi_page':   ('div.meneame',),
        'remove_tags':  ('div.main_k', '#Tab3', '#logoutblock', '#loginblock', 'div[class="pre"]', 'p[class="clear"]',
                         'div.con_wei', re.compile(r'content_biaoqian2.*?div style="background', re.S)),
        'details':
            {
                'pyq_title':        ('h1[class="left"]', ),
                'pyq_date_author': {
                    'date': ("div.contentbiao", ),
                    'auth': ('div.contentbiao span.blue', )
                },
                'pyq_content':      ('#zoom', )
            }
    },

    {
        'site': 'usa_fx678',
        'urls': [
            {
                'page_url': 'http://www.fx678.com/news/keywords/401015%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'block_attr':   ('div.list_content01.bggrey', ),
        'remove_tags':  (),
        'details':
            {
                'pyq_title':        ('.new_inter_left_position_title', ),
                'pyq_date_author': {
                    'date': (('.new_inter_left_position_title_time', 'span', 0), ),
                    'auth': (('.new_inter_left_position_title_time', 'span', 1), )
                },
                'pyq_content':      ('.wenzhang_my_area > p:first-child', )
            }
    },

]
