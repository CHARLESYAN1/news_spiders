# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .base import Base
from ..utils import write
from ..itemsresolver import TitleResolver
from ..itemsresolver import DateResolver
from ..itemsresolver import AuthResolver
from ..itemsresolver import TextResolver


class NewsSpidersPipeline(Base):
    def close_spider(self, spider):
        self.mongo.disconnect()

    def process_item(self, item, spider):
        url = item['url']
        cat = item['cat']
        title = TitleResolver(item['title']).resolve()
        pub_dt = DateResolver(item['pub_dt'], url).resolve()
        auth = AuthResolver(item['auth'], pub_dt, url, item['reverse']).resolve()
        text = TextResolver(item['text'], url, title=title).resolve()

        which_conf = item['which_conf']
        is_hot = self.segment(spider.config[which_conf]['site']) == 'hot'
        ratio = self.kwf_cls(is_hot, title, url).ratio - 1

        if title and str(pub_dt) and text:
            if is_hot:
                lines = [url, pub_dt, auth, cat, title, text, str(ratio), self.crt]
            else:
                lines = [url, pub_dt, auth, cat, title, text, '0', self.crt]
            write(self.store_path(is_hot), str(pub_dt), lines, url)
            self.insert2mongo(dict(zip(self.required_fields, lines)))
        return item
