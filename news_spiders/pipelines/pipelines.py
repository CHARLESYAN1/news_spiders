# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsSpidersPipeline(object):
    def process_item(self, item, spider):
        print 'item:'
        for text in item['text']:
            print text
            print '*' * 100
        return item
