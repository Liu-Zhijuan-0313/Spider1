# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs


class NovelspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open("novel.csv", "w", "utf-8")
        self.wr = csv.writer(self.file)
        self.wr.writerow(['name', 'url', 'leibie', 'author', 'pub_time', 'status'])

    def process_item(self, item, spider):
        self.wr.writerow([item['name'], item['url'], item['leibie'], item['author'], item['pub_time'], item['status']])
        return item
