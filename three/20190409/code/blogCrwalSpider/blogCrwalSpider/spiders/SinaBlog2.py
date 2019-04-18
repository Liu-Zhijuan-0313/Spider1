# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from blogCrwalSpider.items import BlogcrwalspiderItem


class Sinablog2Spider(CrawlSpider):
    name = 'SinaBlog2'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    # 翻页的链接提取器
    pagelink = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))
    # 帖子详情的链接提取器
    contentlink = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a'))

    rules = [
        Rule(pagelink,follow=True),
        Rule(contentlink,callback='parse_item')
    ]


    def parse_item(self, response):
        item = BlogcrwalspiderItem()
        item['title'] = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        if len(item['title']) > 0:
            item['title'] = item['title'][0]
        else:
            item['title'] = '空'
        item['url'] = response.url
        yield item

