# -*- coding: utf-8 -*-

import re
import time
# from pyquery import PyQuery
import requests

from news_spiders.utils.config import BaseConfigParser
from news_spiders.spiders.common import Collector, BaseCommonSpider
from news_spiders.utils.utils import populate_md5

from scrapy.core.scheduler import Scheduler

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders.crawl import CrawlSpider

# from scrapy.exporters import Ex

from scrapy.crawler import CrawlerProcess, Crawler, CrawlerRunner
from scrapy.http.response.html import HtmlResponse
from scrapy.spiderloader import SpiderLoader
from scrapy import Selector, Request
from scrapy.http.response.html import HtmlResponse


# config = BaseConfigParser(module_path)
# ss = config.get_option_value('specific', 'options')
# print config.get_option_list('specific', 'options')

# spider = BaseCommonSpider('hot_nbd')
# print spider.start_urls
# crawler = CrawlerProcess()
# crawler.crawl(BaseCommonSpider, 'hot_nbd')
# crawler.start()


# from news_spiders.extractors.text import TextExtractors
# from news_spiders.extractors.base import ResponseProcessor, BaseMarks

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
            },
        'is_script': True,
    }

url = 'http://money.163.com/16/0308/12/BHKT6Q2300253B0H.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/48.0.2564.116 Safari/537.36'
}
# text = requests.get(url, headers=headers).content.decode('gb18030').encode('u8')
# print text.decode('gb18030').encode('u8')

# t = TextExtractors(Selector(text=text), conf)

# print t.title
# print t.date
# print t.auth
# print t.reverse
# print t.text
# print t.removal

# rp = ResponseProcessor(Selector(text=u'123'))

sss =u"""
<html>
<ul class="ntes-nav-select-list">
                <li>
                    <a href="http://www.kaola.com/outter/promote/myzq.html"><span>母婴专区</span></a>
                </li>
                <li>
                    <a href="http://www.kaola.com/outter/promote/mrcz.html"><span>美容彩妆</span></a>
                </li>
                <li>
                    <a href="http://www.kaola.com/outter/promote/jjry.html"><span>家居日用</span></a>
                </li>
                <li class="usa">
                    <a href="http://www.kaola.com/outter/promote/jkms.html"><span>进口美食</span></a>
                </li>
                <li class="ggg">
                    <a href="http://www.kaola.com/outter/promote/yybj.html"><span>营养保健</span></a>
                </li>
                <li class="gg">
                    <a href="http://www.kaola.com/outter/promote/hwzy.html"><span>海外直邮</span></a>
                </li>
                </ul>
</html>
"""

se = Selector(text=sss)

# from news_spiders.extractors.extensions import SlrExtensions
# np = SlrExtensions(se).test('li.ggg')
# print ''.join(np.xpath('//text()').extract())
# print ''.join(se.css('li.ggg')[0].xpath('.//text()').extract())
# print '_' * 100
# print ''.join(se.xpath('//li[@class="ggg"]').extract())
# print '+' * 100
# print ''.join(se.xpath("""//*[set:difference(node(), //li[@class="ggg"])]/text()""").extract())  # remove(//li[@class="ggg"])

# print se._root, type(se._root)
# print 'a:', dir(se._root)
# sr = se._root.xpath('//li[@class="usa"]')[0]
# print se, type(sr)
# print sr, sr.clear()
# # print se._root.xpath('//ul')[0].text
# for _rt in  se._root.xpath('//*/text()'):
#     if _rt.strip():
#         print '22:', _rt.strip()

from lxml.etree import _Element

from news_spiders.spiders.news_spiders import NewsSpiders
from news_spiders.settings import settings
_settings = {_attr: getattr(settings, _attr) for _attr in dir(settings) if not _attr.startswith('_')}
print _settings

# uurl = 'http://www.2258.com/news/hgjj/1441749.html'
# uurl = 'http://www.2258.com/news/local/196919'
uurl = 'http://finance.sina.com.cn/china/gncj/2016-03-15/doc-ifxqhmvc2463964.shtml'
crawler = CrawlerProcess(settings=_settings)
crawler.crawl(NewsSpiders, name='hot_sina', url=uurl)
crawler.start()

from twisted.internet import reactor
# while True:
# runner = CrawlerRunner()
# runner.crawl(NewsSpiders, name='hot_sina', url=uurl)
# d = runner.join()
# d.addBoth(lambda _: reactor.stop())
#
# reactor.run()

# from news_spiders.conf import InitConfigs
# print 'hah:', InitConfigs().settings

