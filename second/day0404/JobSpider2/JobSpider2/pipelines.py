# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs


class Jobspider2Pipeline(object):
    def __init__(self):
        self.file = codecs.open("tencent.csv", "w", "utf-8")
        self.wr = csv.writer(self.file)
        self.wr.writerow(['position', 'Job_category',  'people_number', 'site', 'time'])

    def process_item(self, item, spider):
        self.wr.writerow([item['position'], item['Job_category'], item['people_number'], item['site'], item['time']])
        return item

    def close_spider(self, item, spider):
        self.file.close()
