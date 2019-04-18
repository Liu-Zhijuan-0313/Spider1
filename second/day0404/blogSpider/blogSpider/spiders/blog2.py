# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from blogSpider.items import BlogspiderItem


class Blog2Spider(CrawlSpider):
    name = 'blog2'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']
    "翻页"
    pagelink = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))
    contentlink = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a'))
    rules = [
        Rule(pagelink, follow=True),
        Rule(contentlink, callback='parse_item')
    ]

    def parse_item(self, response):
        title1 = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        if len(title1) > 0:
            title = title1[0]
        else:
            title = "空"
        print("标题：", title)
        url = response.url
        print("链接：", url)
