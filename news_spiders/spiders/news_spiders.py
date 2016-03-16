from scrapy import Request, Selector

from . import common
from ..items import NewsSpidersItem
from ..extractors import NewsExtractor


class NewsSpiders(common.BaseCommonSpider):
    required_fields = ['url', 'title', 'pub_dt', 'auth', 'text', 'reverse', 'which_conf', 'cat']

    @staticmethod
    def next_request(meta):
        return meta.get('next_request', False)

    def parse_news(self, response):
        meta = response.meta
        config_key = meta[self.conf_key]

        extractor = NewsExtractor(Selector(response), config=self.config[config_key])

        if self.next_request(meta) is False:
            meta.update({
                'which_conf': config_key,
                'url': response.url,
                'title': extractor.title,
                'pub_dt': extractor.date or meta.get('pub_dt'),
                'auth': extractor.auth or meta.get('auth', u''),
                'text': [extractor.text],
                'reverse': extractor.marks_reverse,
                'next_urls': extractor.pagination_urls,
                'cat': self.config[config_key]['cate'],
            })
        elif self.next_request(meta) is None:
            # If have multi pages news content, here yield pipelines, including two or more pages
            meta['text'].append(extractor.text)
            news_item = {k: v for k, v in meta.iteritems() if k in self.required_fields}
            yield NewsSpidersItem(**news_item)
        print 'urls:', meta['next_urls']

        if meta['next_urls']:
            next_url = meta['next_urls'][0]
            meta['next_urls'] = next_urls = meta['next_urls'][1:]
            print 'next_url:', next_url, self.next_request(meta), len(next_urls)

            if self.next_request(meta) is False:
                # guarantee `next_request` is True and  first page news content don't append `text` field
                meta['next_request'] = True
            elif self.next_request(meta) is True:
                # guarantee to append news content to `text` field when not the first page and last page
                meta['text'].append(extractor.text)

            if not next_urls:
                meta['next_request'] = None

            yield Request(url=next_url, callback=self.parse_news, meta=meta)
        elif self.next_request(meta) is False:
            # If just only one page news content, here yield pipelines
            news_item = {k: v for k, v in meta.iteritems() if k in self.required_fields}
            yield NewsSpidersItem(**news_item)


