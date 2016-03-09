from datetime import datetime

from scrapy import Request
from scrapy.loader import ItemLoader

from ..items import NewsSpidersItem
from .common import BaseCommonSpider
from ..extractors import TextExtractors


class NewsSpiders(BaseCommonSpider):
        @property
        def crt(self):
            return str(datetime.now()).replace('-', '').replace(' ', '').replace(':', '')[:14]

        def parse_news(self, response):
            conf_value = response.meta[self.settings['CONFIG_KEY']]
            config = self.config[conf_value]

            multipage_urls = []
            text = ''

            for _each_multipage_url in multipage_urls:
                yield Request(
                    url=_each_multipage_url,
                    callback=self.parse_news,
                    meta={self.conf_key: conf_value, 'text': text}
                )

            item_loader = ItemLoader(item=NewsSpidersItem(), response=response)
            item_loader.add_value('url', response.url)
            item_loader.add_value('crt', self.crt)
            item_loader.add_value('ratio', 1)
            item_loader.add_css('title', )

            yield item_loader.load_item()
