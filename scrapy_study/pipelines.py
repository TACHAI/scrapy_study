# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyStudyPipeline(object):
    def process_item(self, item, spider):

        item["hello"] = "world"
        # spider还有属性名 可以用来判断
        # spider.name == "itcast"
        if item["come_from"]=="itcast":
            print(item)

        return item


class ScrapyStudyPipeline1(object):
    def process_item(self, item, spider):
        # TODO
        print(item)
        return item
