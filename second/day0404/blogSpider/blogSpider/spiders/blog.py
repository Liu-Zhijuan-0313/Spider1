# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from blogSpider.items import BlogspiderItem


class BlogSpider(CrawlSpider):
    name = 'blog'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/blog_5af303e30102yb5x.html']
    "三种方法：xpath,css选择器,re正则"
    # articlelink = LinkExtractor(restrict_xpaths=('//div[@class="articalfrontback SG_j_linedot1 clearfix"]//a'))
    # articlelink = LinkExtractor(restrict_css=('div[class="articalfrontback SG_j_linedot1 clearfix"] a'))
    articlelink = LinkExtractor(allow=("/s/blog_.*?\.html"))
    "设定回调函数，follow默认为flase,自己设为true，自动跟进请求"

    rules = [
        Rule(articlelink, callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        title1 = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        if len(title1)>0:
            title = title1[0]
        else:
            title = "空"
        print("标题：", title)
        url = response.url
        print("链接：", url)
        item = BlogspiderItem()


