# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import csv
import codecs


class SunspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open("sun.csv", "w", "utf-8")
        self.wr = csv.writer(self.file)
        self.wr.writerow(['name', 'num',  'link', 'content', 'author', 'pub_time'])

    # def __init__(self):
    #     try:
    #         self.con = pymysql.Connect(host='localhost', user='root', password="123456",
    #                      database='goods', port=3306)
    #         self.cur = self.con.cursor()
    #     except Exception as e:
    #         print(e)

    def process_item(self, item, spider):
        self.wr.writerow([item['name'], item['num'], item['link'], item['content'], item['author'], item['pub_time']])

        # try:
        #     sql = "insert into sun0769 VALUES(0, %s, %s, %s, %s, %s, %s)"
        #     params = [item['name'], item['num'], item['link'], item['content'], item['author'], item['pub_time']]
        #     count = self.cur.execute(sql, params)
        #     self.con.commit()
        # except Exception as e:
        #     print(e)
        return item

    def close_spider(self, item, spider):
        # self.cur.close()
        # self.con.close()
        self.file.close()
