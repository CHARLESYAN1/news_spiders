# -*- coding: utf-8 -*-

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
]











