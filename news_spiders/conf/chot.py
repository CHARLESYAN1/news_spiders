# -*- coding: utf-8 -*-

import re

HOT_CONFIGS = [
    # # JD hot news end
    {
        'site': 'hot_ifeng',
        'urls': [
            {
                'page_url': 'http://finance.ifeng.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hjd'
            },
        ],
        'block_attr':   ('.box_01', '.box_02', ),
        'remove_tags': ('.picIntro', 'p[style="text-align: center;"]', 'style', 'script'),
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
        'site': 'hot_sina',
        'urls': [
            {
                'page_url': 'http://finance.sina.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hjd'
            },
        ],
        'block_attr':   ('#blk_hdline_01', '.m-p1-mb1-list', ),
        'remove_tags': ('.img_descr', '.finance_app_zqtg', '.xb_new_finance_app',
                        '.otherContent_01', '.hqimg_related', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#artibodyTitle', ),
                'pyq_date_author':   {
                    'date': ('.time-source', '#pub_date'),
                    'auth': ('.time-source', 'span[data-sudaclick="media_name"]', '#media_name')
                },
                'pyq_content':  (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S), '#artibody')
            }
    },

    {
        'site': 'hot_sina_json',
        'urls': [
            {
                'page_url': 'http://top.finance.sina.com.cn/ws/GetTopDataList.php?top_not_url=/stock/|/money/&'
                            'top_type=day&top_cat=finance_0_suda&top_time=%s&top_show_num=10&top_order=DESC&get_new=1',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hjd'
            },
        ],
        'remove_tags': ('.img_descr', '.finance_app_zqtg', '.xb_new_finance_app',
                        '.otherContent_01', '[data-sudaclick="suda_1028_guba"]', 'style', 'script'),
        'json': {
            'data_key': 'data',
            'url_key': 'url'
        },
        'details':
            {
                'pyq_title':        ('#artibodyTitle', ),
                'pyq_date_author':   {
                    'date': ('.time-source', ),
                    'auth': ('span[data-sudaclick="media_name"]', '.time-source')
                },
                'pyq_content':  (re.compile(r'<!-- publish_helper.*?>(.*?)<!-- publish_helper_end -->', re.S),
                                 '#artibody',
                                 )
            }
    },


    {
        'site': 'hot_qq',
        'urls': [
            {
                'page_url': 'http://finance.qq.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hjd'
            },
        ],
        'block_attr':   ('div[bosszone="NewsFocus1"]', 'ul[bosszone="NewsFocus2"]'),
        'remove_tags': ('.pictext', '#invideocon', '.rv-root-v2.rv-js-root', 'script', 'style'),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('.pubTime', ),
                    'auth': ('.where', )
                },
                'pyq_content':      ('#Cnt-Main-Article-QQ',)
            }
    },

    {
        'site': 'hot_nbd',
        'urls': [
            {
                'page_url': 'http://www.nbd.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hjd'
            },
        ],
        'block_attr': ('#top-line-ul', '.news-list',
                       ('ul[style="overflow: hidden; visibility: visible; position: inherit; height: auto;"]', 0),
                       ('ul[style="overflow: hidden; visibility: visible; position: inherit; height: auto;"]', 2),
                       ('ul[style="overflow: hidden; visibility: visible; position: inherit; height: auto;"]', 3),
                       ),
        'remove_tags':  ('ul[class="right fr"]', '.pagination', '.articleInfo', '.articleCopyright'),
        'details':
            {
                'pyq_title':        (('span[class="fl"]', 0), ),
                'pyq_date_author':  {
                    'date': ('.left', ),
                    'auth': (re.compile(r'<ul class="left">.*?source\.png.*?<span>(.*?)</span>', re.S), )
                },
                'pyq_content':      ('.main-left-article', )
            }
    },

    {
        'site': 'hot_stcn',
        'urls': [
            {
                'page_url': 'http://www.stcn.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hjd'
            },
        ],
        'remove_tags':  ('.setFZ', '.om', 'script'),
        'block_attr': ('.hotNews', '#listwrap'),
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
        'site': 'hot_xinhuanet',
        'urls': [
            {
                'page_url': 'http://www.news.cn/fortune/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hjd'
            },
        ],
        'remove_tags':  ('script', 'style'),
        'block_attr': ('.textList', ),
        'details':
            {
                'pyq_title':        ('#title', ),
                'pyq_date_author':  {
                    'date': ('.time', ),
                    'auth': ('#source', )
                },
                'pyq_content':      ('.article', )
            }
    },

    {
        'site': 'hot_sohu',
        'urls': [
            {
                'page_url': 'http://business.sohu.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.news', ),
        'remove_tags': ('.stockTrends',),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu', ),
                    'auth': ("#media_span", )
                },
                'pyq_content':      ('[itemprop="articleBody"]', )
            }
    },

    {
        'site': 'hot_163',
        'urls': [
            {
                'page_url': 'http://money.163.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr': ('.fn_focus_news', '.fn_three_cat'),
        'remove_tags': (re.compile(r'<!--biaoqian.*?>.*?<!--biaoqian.*?>', re.S),
                        'div[class="ep-source cDGray"]', '.nph_photo', '.nph_photo_ctrl',
                        '.nvt_vote_2', '.demoBox', '.hidden', 'script', 'style'),
        'details':
            {
                'pyq_title':        (('#h1title', 0), ('h1', 0)),
                'pyq_date_author':  {
                    'date': ('.ep-time-soure', '.post_time_source'),
                    'auth': ("#ne_article_source", )
                },
                'pyq_content':      ('#endText', )
            }
    },
    # JD hot news end

    # zhitou hot news start
    {
        'site': 'hot_cnstock',
        'urls': [
            {
                'page_url': 'http://www.cnstock.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://news.cnstock.com/bwsd/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.m-left', '#bw-list'),
        'multi_page':   ('#contentPager',),
        'remove_tags':  ('u', ),
        'details':
            {
                'pyq_title':        ('.title', ),
                'pyq_date_author':  {
                    'date': ('.timer', ),
                    'auth': ('.source', )
                },
                'pyq_content':      ('#qmt_content_div', )
            }
    },

    {
        'site': 'hot_yicai',
        'urls': [
            {
                'page_url': 'http://www.yicai.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.headline', 'h1', ),
        'remove_tags':  ('p[style="text-align: center;"]', 'p[style="text-align:center"]'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_author_date':  {
                    'date': (('h2', None, 0), ),
                    'auth': (('h2', None, 0), ),
                },
                'pyq_content':      ('.tline', )
            }
    },

    {
        'site': 'hot_caixin',
        'urls': [
            {
                'page_url': 'http://economy.caixin.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://finance.caixin.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://companies.caixin.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('#listArticle', ),
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
        'site': 'hot_wallstreetcn',
        'urls': [
            {
                'page_url': 'http://wallstreetcn.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('a[class="title"]',),
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
        'site': 'hot_eeo',
        'urls': [
            {
                'page_url': 'http://www.eeo.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   (('.e_i_jdt_bg_1', 0), ('.e_i_jdt_bg_1', 3)),
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
        'site': 'hot_hexun',
        'urls': [
            {
                'page_url': 'http://www.hexun.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr': ('#con_ystab_1', ),
        'remove_tags': ('font', '[style="text-align:right;font-size:12px"]', 'style', 'script'),
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
        'site': 'hot_2258',
        'urls': [
            {
                'page_url': 'http://www.2258.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'multi_page':    ('.paging',),
        'block_attr':   ('.tci_img', ),
        'details':
            {
                'pyq_title':        ('h1.a_tit',),
                'pyq_date_author':  {
                    'date': ('.ac_from', ),
                    'auth': ('.ac_from',)
                },
                'pyq_content':      ('.a_word', )
            }
    },

    {
        'site': 'hot_p5w',
        'urls': [
            {
                'page_url': 'http://www.p5w.net/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr': ('div[class="news-title title"]', 'dl[class="yw"]'),
        'remove_tags': ('#_Custom_V6_Style_', 'style',),
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
        'site': 'hot_caijing',
        'urls': [
            {
                'page_url': 'http://www.caijing.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr': ('#area_index_jrtt_2011', '#area_index_cjyw_2011'),
        'remove_tags': ('.ar_writer', '.ar_keywords',),
        'details':
            {
                'pyq_title':        ('#cont_title',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu',),
                },
                'pyq_content':      ('#the_content', )
            }
    },

    {
        'site': 'hot_people',
        'urls': [
            {
                'page_url': 'http://finance.people.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr': ('.p2_left', ),
        'remove_tags': ('.pictext', ),
        'details':
            {
                'pyq_title':        ('#p_title', ),
                'pyq_date_author':  {
                    'date': ('#p_publishtime', ),
                    'auth': ("#p_origin", )
                },
                'pyq_content':  ('#p_content', )
            }
    },

    {
        'site': 'hot_xinhua08',
        'urls': [
            {
                'page_url': 'http://news.xinhua08.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr': ('div[class="col-sm-6 col-md-4 headlines mainnews c3-md-4"]', '#latest'),
        'remove_tags': ('font', 'style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_author_date':  {
                    'date': (('.pull-left', None, 0), ),
                    'auth': (('.pull-left', None, 0), ),
                },
                'pyq_content':      ('#ctrlfscont', )
            }
    },

    {
        'site': 'hot_cnfol',
        'urls': [
            {
                'page_url': 'http://news.cnfol.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'multi_page': ('#page', ),
        'block_attr': ('.Inews', 'div[class="Tlnew Conwh Mt10"]', 'div[class="Tnew2"]'),
        'remove_tags': ('.text-pic-tt', 'style', 'script'),
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
        'site': 'hot_thepaper',
        'urls': [
            {
                'page_url': 'http://www.thepaper.cn/channel_masonry.jsp?channelID=25951%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr': ('h2',),
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
        'site': 'hot_cs',
        'urls': [
            {
                'page_url': 'http://www.cs.com.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   (".big_news", '.box_line1_r',),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        (('h1', 1), ),
                'pyq_date_author':  {
                    'date': ('.ctime01', ),
                    'auth': (('.Atext', None, 1), )
                },
                'pyq_content':  ('.Dtext', )
            }
    },

    {
        'site': 'hot_21jingji',
        'urls': [
            {
                'page_url': 'http://www.21jingji.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('#MainNews h2', '#MainNews h3', '#MainNews .TitleLink.F12', (".Selections", 0)),
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
        'site': 'hot_emoney',
        'urls': [
            {
                'page_url': 'http://www.emoney.cn/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('div[class="nro bbdt"]', ('[class="nro"]', 0)),
        'multi_page':    ('#cpage',),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('.newsTitle2', ),
                'pyq_author_date':  {
                    'date': (('.p1', None, 0), ),
                    'auth': ()
                },
                'pyq_content':  ('.content', )
            }
    },

    {
        'site': 'hot_opsteel',
        'urls': [
            {
                'page_url': 'http://www.opsteel.cn/news/gnyw%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.opsteel.cn/news/cjsx%s.html',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
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
        'site': 'hot_cailianpress',
        'urls': [
            {
                'page_url': 'http://www.cailianpress.com/subject/%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.cailianpress.com/depth/%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.title', ),
        'remove_tags': ('.state', 'style', 'script'),
        'details':
            {
                'pyq_title':        ('#title', ),
                'pyq_date_author':  {
                    'date': ('span.time', ),
                    'auth': ()
                },
                'pyq_content':  ('#entries li.content', )
            }
    },

    {
        'site': 'hot_pbc',
        'urls': [
            {
                'page_url': 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.pbc.gov.cn/goutongjiaoliu/113456/2164857/b4612a9a/index%s.html',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.newslist_style', ),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('h2', ),
                'pyq_date_author':  {
                    'date': ('td[class="hui12"][align="right"]', ),
                    'auth': ('td[class="hui12"][align="center"]', )
                },
                'pyq_content':  ('#zoom', )
            }
    },

    # {
    #     'site': 'hot_mof',
    #     'urls': [
    #         {
    #             'page_url': 'http://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/%s',
    #             'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
    #         },
    #
    #         {
    #             'page_url': 'http://www.mof.gov.cn/zhengwuxinxi/zhengcejiedu/%s',
    #             'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
    #         },
    #     ],
    #     'block_attr':   ('.ZITI', ),
    #     'remove_tags': ('style', 'script'),
    #     'details':
    #         {
    #             'pyq_title':        ('.font_biao1', ),
    #             'pyq_date_author':  {
    #                 'date': (('p[align="right"]', None, 1), ),
    #                 'auth': ()
    #             },
    #             'pyq_content':  ('#Zoom', )
    #         }
    # },

    {
        'site': 'hot_stats',
        'urls': [
            {
                'page_url': 'http://www.stats.gov.cn/tjsj/sjjd/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.center_list_contlist', '.center_list_cont'),
        'remove_tags': ('style', 'script'),
        'details':
            {
                'pyq_title':        ('.xilan_tit', ),
                'pyq_date_author':  {
                    'date': ('font.xilan_titf', ),
                    'auth': ('font.xilan_titf > font > font', )
                },
                'pyq_content':  ('.xilan_con', )
            }
    },

    {
        'site': 'hot_mofcom',
        'urls': [
            {
                'page_url': 'http://www.mofcom.gov.cn/article/ae/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   (('.listBox ul', 0),),
        'remove_tags': (),
        'is_script': False,
        'details':
            {
                'pyq_title':        ('#artitle', ),
                'pyq_date_author':  {
                    'date': (re.compile(r'var tm = "(.*?)"', re.S), ),
                    'auth': (re.compile(r'var source = "(.*?)"', re.S), )
                },
                'pyq_content':  ('#zoom', )
            }
    },

    {
        'site': 'hot_haiwainet',
        'urls': [
            {
                'page_url': 'http://finance.haiwainet.cn/352346/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('[class="ul04 ub01 pt10 upton"]', ),
        'multi_page':   ('.zdfy',),
        'remove_tags':  (re.compile(r'<div class="zdfy.*?>.*?</div>', re.S), '#editor_baidu'),
        'details':
            {
                'pyq_title':        ('.H01',),
                'pyq_date_author':  {
                    'date': ('#pubtime_baidu',),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#con',)
            }
    },

    {
        'site': 'hot_chinadaily',
        'urls': [
            {
                'page_url': 'http://caijing.chinadaily.com.cn/node_1078506.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.bt1', ),
        'remove_tags':  (),
        'details':
            {
                'pyq_title':        ('#title',),
                'pyq_date_author':  {
                    'date': ('.arcform',),
                    'auth': ('#source_baidu', )
                },
                'pyq_content':      ('#Zoom',)
            }
    },

    {
        'site': 'hot_yzforex',
        'urls': [
            {
                'page_url': 'http://www.yzforex.com/index.php?m=content&c=index&a=lists&catid=21%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.m-list', ),
        'remove_tags':  ('#comment', '#hits'),
        'details':
            {
                'pyq_title':        (re.compile(r'<h1>(.*?)_.*?<br', re.S),),
                'pyq_date_author':  {
                    'date': ('h1 span',),
                    'auth': ('h1 span', )
                },
                'pyq_content':      ('.content',)
            }
    },

    {
        'site': 'hot_ftchinese',
        'urls': [
            {
                'page_url': 'http://www.ftchinese.com/channel/chinaeconomy.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.ftchinese.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/chinastock.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/chinareport.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/chinabusiness.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/chinamarkets.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://www.ftchinese.com/channel/chinaopinion.html%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('a.thl', '#column1'),
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
        'site': 'hot_qq_lenjing',
        'urls': [
            {
                'page_url': 'http://finance.qq.com/prism.htm%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   (re.compile(r'div class="tit".*?<a.*?href="(?P<url>.*?)".*?</div>.*?'
                                    r'span class="aTime">(?P<date>.*?)</span>', re.S), ),
        'remove_tags': ('h1 span', ),
        'details':
            {
                'pyq_title':        ('h1', ),
                'pyq_author_date':  {
                    'date': (),
                    'auth': ()
                },
                'pyq_content':  ('#articleContent', )
            }
    },

    {
        'site': 'hot_jiemian',
        'urls': [
            {
                'page_url': 'http://www.jiemian.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.columns-left h3', '.columns.columns-center > div:nth-child(2) h3'),
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
        'site': 'hot_takungpao',
        'urls': [
            {
                'page_url': 'http://finance.takungpao.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('.news_txt',),
        'remove_tags':  ('p[style="text-align: center"]', '.pictext'),
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
        'site': 'hot_kxt',
        'urls': [
            {
                'page_url': 'http://www.kxt.com/news%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'block_attr':   ('p.red_line', 'a.yk_a'),
        'remove_tags':  ('ul#share', 'p[style="text-align:center;text-indent:0;"]'),
        'details':
            {
                'pyq_title':        (('h1', 0), ),
                'pyq_date_author':  {
                    'date': ('.g_tag', ),
                    'auth': (),
                },
                'pyq_content':      ('div.content > p', )
            }
    },

]
