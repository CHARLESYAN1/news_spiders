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
        extractor = NewsExtractor(Selector(response), config=self.config[meta[self.conf_key]])

        if not self.next_request(meta):
            pagination_urls = extractor.pagination_urls
            results.update(
                {
                    'url': response.url,
                    'title': extractor.title,
                    'pub_dt': extractor.date,
                    'auth': extractor.auth,
                    'text': extractor.text,
                    'reverse': extractor.marks_reverse
                }
            )

        if not pagination_urls:
            yield NewsSpidersItem(**results)
        else:
            for _page_url in pagination_urls:
                meta.update(next_request=True, **results)
                meta['text'] = meta['text'] + extractor.text

                yield Request(url=_page_url, callback=self.parse_news, meta=meta)




