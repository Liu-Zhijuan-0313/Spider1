# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Jobspider2Item(scrapy.Item):
    # define the fields for your item here like:\
    "招聘岗位，类别，人数，城市，发布日期"
    position = scrapy.Field()
    Job_category = scrapy.Field()
    people_number = scrapy.Field()
    site = scrapy.Field()
    time = scrapy.Field()
