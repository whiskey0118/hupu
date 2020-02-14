# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class HupuPipeline(object):
    collectionName = 'hupu'

    def __init__(self,mongoUrl,mongoDb):
        self.mongoUrl = mongoUrl
        self.mongoDb = mongoDb

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongoUrl=crawler.settings.get("MONGO_URI"),
            mongoDb = crawler.settings.get('MONGO_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongoUrl)
        self.db = self.client[self.mongoDb]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collectionName].insert_one(dict(item))

