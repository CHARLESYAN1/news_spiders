# -*- coding: utf-8 -*-

import re
import time
from pyquery import PyQuery
import requests

from news_spiders.utils.config import BaseConfigParser
from news_spiders.conf.genconf import module_path
from news_spiders.spiders.common import Collector, BaseCommonSpider
from news_spiders.utils.utils import populate_md5

from scrapy.core.scheduler import Scheduler

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders.crawl import CrawlSpider

from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.http.response.html import HtmlResponse
from scrapy.spiderloader import SpiderLoader
from scrapy import Selector
from scrapy.http.response.html import HtmlResponse


# config = BaseConfigParser(module_path)
# ss = config.get_option_value('specific', 'options')
# print config.get_option_list('specific', 'options')

# spider = BaseCommonSpider('hot_nbd')
# print spider.start_urls
# crawler = CrawlerProcess()
# crawler.crawl(BaseCommonSpider, 'hot_nbd')
# crawler.start()


from news_spiders.extractors.text import BaseMarks, TextExtractors

conf = {
        'site': 'hot_money163',
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
                'pyq_title':        (('#h1title', 0), ),
                'pyq_date_author':  {
                    'date': ('.ep-time-soure', ),
                    'auth': ("#ne_article_source", )
                },
                'pyq_content':      ('#endText', )
            }
    }

url = 'http://money.163.com/16/0308/12/BHKT6Q2300253B0H.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/48.0.2564.116 Safari/537.36'
}
text = requests.get(url, headers=headers).content.decode('gb18030').encode('u8')
# print text.decode('gb18030').encode('u8')

t = TextExtractors(Selector(text=text), conf)

# print t.title
# print t.date
# print t.auth
# print t.reverse
print t.text
# print t.removal


