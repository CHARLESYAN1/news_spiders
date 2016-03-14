# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsSpidersItem(scrapy.Item):
    url = scrapy.Field()
    which_conf = scrapy.Field()
    pub_dt = scrapy.Field()
    auth = scrapy.Field()
    cat = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    reverse = scrapy.Field()
