# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class SunspiderPipeline(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='sundb1811',charset='utf8')
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)


    def process_item(self, item, spider):
        try:
            sql = 'insert into sun0769 VALUES (0,%s,%s,%s,%s,%s,%s)'
            params = [item['name'],item['number'],item['url'],item['content'],item['author'],item['pub_date']]
            count = self.cur.execute(sql,params)
            self.conn.commit()
        except Exception as e:
            print(e)
        return item

    def close_spider(self,item,spider):
        self.cur.close()
        self.conn.close()
