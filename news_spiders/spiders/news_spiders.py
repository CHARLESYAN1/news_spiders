from datetime import datetime

from scrapy import Request, Selector
from scrapy.loader import ItemLoader

from ..items import NewsSpidersItem
from .common import BaseCommonSpider
from ..extractors import NewsExtractor


class NewsSpiders(BaseCommonSpider):
    required_fields = ['url', 'title', 'pub_dt', 'auth', 'text', 'reverse']

    @staticmethod
    def next_request(meta):
        return meta.get('next_request', False)

    def parse_news(self, response):
        results = {}
        pagination_urls = []
        meta = response.meta
        # print 'meta:', meta
        extractor = NewsExtractor(Selector(response), config=self.config[meta[self.conf_key]])

        if self.next_request(meta) is False:
            # pagination_urls = extractor.pagination_urls
            meta.update(
                {
                    'url': response.url,
                    'title': extractor.title,
                    'pub_dt': extractor.date,
                    'auth': extractor.auth,
                    'text': [extractor.text],
                    'reverse': extractor.marks_reverse,
                    'next_urls': extractor.pagination_urls
                }
            )

            news_item = {k: v for k, v in meta.iteritems() if k in self.required_fields}
            yield NewsSpidersItem(**news_item)
        elif self.next_request(meta) is None:
            meta['text'].append(extractor.text)
            news_item = {k: v for k, v in meta.iteritems() if k in self.required_fields}
            yield NewsSpidersItem(**news_item)
        print 'urls:', meta['next_urls']

        if meta['next_urls']:
            next_url = meta['next_urls'][0]
            meta['next_urls'] = next_urls = meta['next_urls'][1:]
            print 'next_url:', next_url, self.next_request(meta)

            if self.next_request(meta) is False:
                meta['next_request'] = True
            elif not next_urls:
                meta['next_request'] = None
            else:
                meta['text'].append(extractor.text)

            yield Request(url=next_url, callback=self.parse_news, meta=meta)


