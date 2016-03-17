# -*- coding: utf-8 -*-

import re

HIF_CONFIGS = [
    {
        'site': 'hif_huagu',
        'urls': [
            {
                'page_url': 'http://www.huagu.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   (('.box_Bj2', 0), ('.list3', 0), ('.list3', 1)),
        'remove_tags':  ('select', re.compile(r'<div class="page">.*?<.div>', re.S)),
        'multi_page':   ('.page', ),
        'details':
            {
                'pyq_title':        ('#h1-title',),
                'pyq_date_author':  {
                    'date': ('.info',),
                    'auth': ('.where',)
                },
                'pyq_content':      ('#div-article-content', )
            }
    },

    {
        'site': 'hif_huanqiu',
        'urls': [
            {
                'page_url': 'http://finance.huanqiu.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.newsFir', ),
        'remove_tags': ('#editor_baidu', '.reTopics'),
        'details':
            {
                'pyq_title':        (('h1', 0),),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',)
                },
                'pyq_content':      ('#text', )
            }
    },

    {
        'site': 'hif_fx678',
        'urls': [
            {
                'page_url': 'http://news.fx678.com/news/top/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.touzi_font', ),
        'remove_tags': (),
        'details':
            {
                'pyq_title':        ('.new_inter_left_position_title',),
                'pyq_date_author':  {
                    'date': ('.new_inter_left_position_title_time',),
                    'auth': ('.new_inter_left_position_title_time',)
                },
                'pyq_content':      (('.wenzhang_my_area', 'p'), )
            }
    },

    {
        'site': 'hif_21so',
        'urls': [
            {
                'page_url': 'http://stocks.21so.com/agu/index%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://www.21so.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
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
        'site': 'hif_jfinfo',
        'urls': [
            {
                'page_url': 'http://stock.jfinfo.com/tzfxb/index%s.shtml',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'multi_page': ('.pageNum',),
        'block_attr':   ('.listBlock', ),
        'remove_tags': ('.editerEnter', ),
        'details':
            {
                'pyq_title':        (('h1', 0),),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',)
                },
                'pyq_content':      ('.articleCont', )
            }
    },

    {
        'site': 'hif_17ok',
        'urls': [
            {
                'page_url': 'http://stock.17ok.com/list.php?id=335%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
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
        'site': 'hif_ourku',
        'urls': [
            {
                'page_url': 'http://www.ourku.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://news.ourku.com/html/zq_news/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.contentlist', '#table_news'),
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
        'site': 'hif_qianzhan',
        'urls': [
            {
                'page_url': 'http://www.qianzhan.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'multi_page':   ('.page',),
        'block_attr':   ('.headline', '.focus_main'),
        'details':
            {
                'pyq_title':        (('h1', 0),),
                'pyq_date_author':  {
                    'date': ('.author-time',),
                    'auth': ('.article-info-source',)
                },
                'pyq_content':      ('.article-details', )
            }
    },

    {
        'site': 'hif_yingfu001',
        'urls': [
            {
                'page_url': 'http://www.yingfu001.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.tit1', '.title1', '.title1-1'),
        'details':
            {
                'pyq_title':        ('.title',),
                'pyq_date_author':  {
                    'date': ('.title2l', ),
                    'auth': ('.title2l', ),
                },
                'pyq_content':      ('.txt', )
            }
    },

    {
        'site': 'hif_ceh',
        'urls': [
            {
                'page_url': 'http://www.ceh.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.title_m1', '.jryw_list'),
        'details':
            {
                'pyq_title':        ('.title_content',),
                'pyq_date_author': {
                    'date': ('.date_content',),
                    'auth': ('.date_content',),
                },
                'pyq_content':      (('.content3', None, 1), )
            }
    },

    {
        'site': 'hif_cet',
        'urls': [
            {
                'page_url': 'http://www.cet.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('td[width="889"][height="52"]', 'td[class="font_01"][valign="top"]',
                         'span[class="font_04"]', 'td[width="264"][height="26"][class="font_05"]'),
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
        'site': 'hif_people',
        'urls': [
            {
                'page_url': 'http://finance.people.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.p2_1', 'ul[class="list_14 p2_5 clear"]'),
        'details':
            {
                'pyq_title':        ('#p_title',),
                'pyq_date_author':  {
                    'date': ('#p_publishtime',),
                    'auth': ('#p_origin',)
                },
                'pyq_content':      ('#p_content',)
            }
    },

    {
        'site': 'hif_591hx',
        'urls': [
            {
                'page_url': 'http://www.591hx.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.focusNews',),
        'multi_page':   ('.pagex', ),
        'remove_tags':  ('select', re.compile(r'<div class="pagex">.*?</div>', re.S), 'style', 'script'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.info',),
                    'auth': ('.info',),
                },
                'pyq_content':      ('#newsCon', )
            }
    },

    {
        'site': 'hif_chinanews',
        'urls': [
            {
                'page_url': 'http://finance.chinanews.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   (('.life_left_ul ', 0), ('.life_left_ul ', 1)),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',)
                },
                'pyq_content':      ('.left_zw', )
            }
    },

    {
        'site': 'hif_china',
        'urls': [
            {
                'page_url': 'http://finance.china.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.COT_p1', '.COT_p2', '#jryw_cnt'),
        'details':
            {
                'pyq_title':        (('h1', 2), ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',)
                },
                'pyq_content':      ('#content', )
            }
    },

    {
        'site': 'hif_cnfol',
        'urls': [
            {
                'page_url': 'http://news.cnfol.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'multi_page':   ('#page',),
        'block_attr':   ('.Inews', 'div[class="Tlnew Conwh Mt10"]', '.Tnew2', '.Tco', 'p[class="Tnew2 H120"]'),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ("#Title", ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#Content', )
            }
    },

    {
        'site': 'hif_ce',
        'urls': [
            {
                'page_url': 'http://www.ce.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('.hotnews', ),
        'remove_tags': ('style', 'script'),
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
        'site': 'hif_jrj',
        'urls': [
            {
                'page_url': 'http://www.jrj.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':   ('#S1_M_1', '#S1_M_2', '#S1_M_3', '#S1_M_4'),
        'remove_tags': ('style', 'script'),
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
        'site': 'hif_stcn',
        'urls': [
            {
                'page_url': 'http://www.stcn.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'remove_tags':  ('.setFZ', ),
        'block_attr': ('.hotNews',),
        'details':
            {
                'pyq_title':        (('h2', 0), ),
                'pyq_date_author':  {
                    'date': ('.info', ),
                    'auth': ('.info', ),
                },
                'pyq_content':      ('#ctrlfscont', )
            }
    },

    {
        'site': 'hif_thepaper',
        'urls': [
            {
                'page_url': 'http://www.thepaper.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr': ('.list_hot', ),
        'details':
            {
                'pyq_title':        ('.title_newsinfo', ),
                'pyq_date_author':  {
                    'date': ('.news_other', 'span', ),
                    'auth': ('.news_other', 'a', )
                },
                'pyq_content':      ('.news_txt', )
            }
    },

    {
        'site': 'hif_xinhuanet',
        'urls': [
            {
                'page_url': 'http://www.xinhuanet.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'multi_page':   ('#div_currpage',),
        'block_attr':   ('#hpart2L', '.hots'),
        'remove_tags':  ('.pictext', ),
        'details':
            {
                'pyq_title':        ('#title', ),
                'pyq_date_author': {
                    'date': ('#pubtime', '.time'),
                    'auth': ('#source',),
                },
                'pyq_content':      ('#content', '.article')
            }
    },

    {
        'site': 'hif_ccstock',
        'urls': [
            {
                'page_url': 'http://www.ccstock.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'multi_page':   ('.page',),
        'block_attr':   ('.left1', ),
        'remove_tags':  ('.author', ),
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
        'site': 'hif_stockstart',
        'urls': [
            {
                'page_url': 'http://finance.stockstar.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr': ('.module', '.data-info',),
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
        'site': 'hif_fx168',
        'urls': [
            {
                'page_url': 'http://www.fx168.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr': ('.yjl_fx168_focus_TodayNews', ),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_date_author': {
                    'date': ('.shijian',),
                    'auth': ('.laiyuan', ),
                },
                'pyq_content':      ('.yjl_fx168_article_zhengwen', )
            }
    },

    {
        'site': 'hif_21cn',
        'urls': [
            {
                'page_url': 'http://finance.21cn.com/%s', 'pages': 1, 'first': '',
                'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.fl', ),
        'remove_tags':      ('script', 'style'),
        'details':
            {
                'pyq_title':        ('.title', ),
                'pyq_date_author':  {
                    'date': ('.pubTime',),
                    'auth': ('[rel="nofollow"]',)
                },
                'pyq_content':      ('#article_text', )
            }
    },

    {
        'site': 'hif_jingji',
        'urls': [
            {
                'page_url': 'http://jingji.cntv.cn/data/index.json%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'json': {
            'url_key': 'url',
            'data_key': 'rollData',
        },
        'remove_tags': ('em',),
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
        'site': 'hif_cri',
        'urls': [
            {
                'page_url': 'http://gb.cri.cn/finance/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.cjyw',),
        'details':
            {
                'pyq_title':        ('#ctitle', ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',)
                },
                'pyq_content':  ('#ccontent',)
            }
    },

    {
        'site': 'hif_oeeee',
        'urls': [
            {
                'page_url': 'http://ndfinance.oeeee.com/finance/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.article-li',),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',)
                },
                'pyq_content':  ('#fontzoom',)
            }
    },

    {
        'site': 'hif_huaxi100',
        'urls': [
            {
                'page_url': 'http://news.huaxi100.com/list-242-1%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('#list',),
        'details':
            {
                'pyq_title':        ('.details_title', ),
                'pyq_date_author':  {
                    'date': ('.details_info',),
                    'auth': ('.details_info',),
                },
                'pyq_content':      ('#summary',)
            }
    },

    {
        'site': 'hif_bjnews',
        'urls': [
            {
                'page_url': 'http://finance.bjnews.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.newstitle',),
        'details':
            {
                'pyq_title':        (('h1', 1), ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('.content',)
            }
    },

    {
        'site': 'hif_southcn',
        'urls': [
            {
                'page_url': 'http://finance.southcn.com/f/node_123271.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },

            {
                'page_url': 'http://finance.southcn.com/jrcj/node_188991.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.list',),
        'remove_tags':      ('.pictext',),
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
        'site': 'hif_qiye',
        'urls': [
            {
                'page_url': 'http://www.qiye.gov.cn/news/List_16%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.ns_ul',),
        'remove_tags':      ('.links', ),
        'details':
            {
                'pyq_title':        ('.tit',),
                'pyq_date_author':  {
                    'date': ('.time', ),
                    'auth': (('.time', 'span', 1), ),
                },
                'pyq_content':      ('#zoom',)
            }
    },

    {
        'site': 'hif_newssc',
        'urls': [
            {
                'page_url': 'http://finance.newssc.org/gdxw/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('a[class="black_h"]',),
        'details':
            {
                'pyq_title':        ('h1',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',)
                },
                'pyq_content':      ('section',)
            }
    },

    # {
    #     'site': 'hif_cfi',
    #     'urls': [
    #         {
    #             'page_url': 'http://www.cfi.net.cn/%s',
    #             'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
    #         },
    #     ],
    #     'block_attr':       ('div[style=" float:left;width:380px;margin-left:3px"]',),
    #     'multi_page':   ('#turnpage1',),
    #     'remove_tags':      ('.pictext',),
    #     'details':
    #         {
    #             'pyq_title':        ('h1',),
    #             'pyq_date_author':  {
    #                 'date': ('td[width="40%"]',),
    #                 'auth': ('td[width="40%"]',)
    #             },
    #             'pyq_content':      (re.compile(r'<!--newstext-->(.*?)<!--/newstext-->', re.S),)
    #         }
    # },

    {
        'site': 'hif_10jqka',
        'urls': [
            {
                'page_url': 'http://www.10jqka.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.item.cjyw',),
        'remove_tags':  ('#editor_baidu', 'script', 'style'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author': {
                    'date': ("#pubtime_baidu", '.art_info'),
                    'auth': ('#sourcename', )
                },
                'pyq_content':      ('.art_main', '.atc-content')
            }
    },

    {
        'site': 'hif_nen',
        'urls': [
            {
                'page_url': 'http://finance.nen.com.cn/cj_top_yw/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       (('table[width="100%"]', 0),),
        'remove_tags':      ('.fromwhere', ),
        'details':
            {
                'pyq_title':        ('div.contentt', ),
                'pyq_date_author': {
                    'date': ("#pubtime_baidu", ),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('.contentcon', )
            }
    },

    {
        'site': 'hif_eastday',
        'urls': [
            {
                'page_url': 'http://news.eastday.com/gd2008/finance/index.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
            },
        ],
        'block_attr':       ('.leftsection', ),
        'remove_tags':      ('.pictext', ),
        'details':
            {
                'pyq_title':        ('#biaoti',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu + a', )
                },
                'pyq_content':      ('#zw1',)
            }
    },

    {
        'site': 'hif_ftchinese',
        'urls': [
            {
                'page_url': 'http://www.ftchinese.com/channel/finance.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': u'热点新闻'
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
    }


]
