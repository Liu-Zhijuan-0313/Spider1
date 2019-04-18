# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    "标题，url，阅读数，评论数，转载数"
    title = scrapy.Field()
    url = scrapy.Field()
