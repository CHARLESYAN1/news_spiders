# -*- coding: utf-8 -*-


AMAZON_CONFIGS = [
    {
        'site': 'hot_reuters',
        'urls': [
            {
                'page_url': 'http://cn.reuters.com/%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/chinaNews?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/opinions?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/CNAnalysesNews?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'ori': u'路透中文网',
        'block_attr':   ('#topStory', '#latestHeadlines', 'div[class="feature"]'),
        'multi_page':   ('div.article-paginate', ),
        'remove_tags':  (),
        'details':
            {
                'pyq_title':        ('.article-headline', ),
                'pyq_date_author':  {
                    'date': ('span.timestamp', ),
                    'auth': ()
                },
                'pyq_content':      ('#articleText', )
            }
    },

    {
        'site': 'hot_wsj',
        'urls': [
            {
                'page_url': 'http://cn.wsj.com/gb/index.asp%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'hot'
            },
        ],
        'ori': u'华尔街日报中文网',
        'block_attr':   ('div.balance.column', ),
        'multi_page':   (),
        'remove_tags':  ('div[style="magin:0 3px;width:545px;"]', '#divCopyright'),
        'details':
            {
                'pyq_title':        ('#headline', ),
                'pyq_date_author':  {
                    'date': ('#datetime', ),
                    'auth': ()
                },
                'pyq_content':      ('#A', )
            }
    },

    {
        'site': 'usa_reuters',
        'urls': [
            {
                'page_url': 'http://cn.reuters.com/news/archive/topic-us-ind-equities?view=page&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/topic-us-company?view=page&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_gg'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/topic-us-finance?view=page&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/topic-us-economics?view=page&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/CNIntlBizNews?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/vbc_us_stocks?view=page&page=%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_gs'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/techMediaTelcoNews?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/financialServicesNews?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/healthDrugsNews?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            {
                'page_url': 'http://cn.reuters.com/news/archive/transportationNews?view=page&page=%s&pageSize=10',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },
        ],
        'ori': u'路透中文网',
        'block_attr':   ('#topStory', '#latestHeadlines', 'div[class="feature"]'),
        'multi_page':   ('div.article-paginate', ),
        'remove_tags':  (),
        'details':
            {
                'pyq_title':        ('.article-headline', ),
                'pyq_date_author':  {
                    'date': ('span.timestamp', ),
                    'auth': ()
                },
                'pyq_content':      ('#articleText', )
            }
    },

    {
        'site': 'usa_wsj',
        'urls': [
            {
                'page_url': 'http://cn.wsj.com/gb/usstock.asp%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },

            {
                'page_url': 'http://cn.wsj.com/gb/bus.asp%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://cn.wsj.com/gb/markets.asp%s',
                'pages': 1, 'first': '', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },
        ],
        'ori': u'华尔街日报中文网',
        'block_attr':   ('#t2lnews2', ),
        'multi_page':   (),
        'remove_tags':  ('div[style="magin:0 3px;width:545px;"]', '#divCopyright'),
        'details':
            {
                'pyq_title':        ('#headline', ),
                'pyq_date_author':  {
                    'date': ('#datetime', ),
                    'auth': ()
                },
                'pyq_content':      ('#A', )
            }
    },

    {
        'site': 'usa_nytimes',
        'urls': [
            {
                'page_url': 'http://cn.nytimes.com/usa/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hg'
            },

            {
                'page_url': 'http://cn.nytimes.com/technology/%s',
                'pages': 1, 'first': '%s', 'reverse': None, 'suffix': None, 'cate': 'us_hy'
            },
        ],
        'ori': u'纽约时报中文网',
        'block_attr':   ('.sectionLeadHeader', '.sectionAutoList', ),
        'multi_page':   (),
        'remove_tags':  ('.articleCR', '.authorIdentification'),
        'details':
            {
                'pyq_title':        ('.articleHeadline', ),
                'pyq_date_author':  {
                    'date': ('.byline', ),
                    'auth': ()
                },
                'pyq_content':      ('div.content.chinese', )
            }
    },

]
