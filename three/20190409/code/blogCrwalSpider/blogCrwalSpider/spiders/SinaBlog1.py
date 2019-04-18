# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from blogCrwalSpider.items import BlogcrwalspiderItem

class Sinablog1Spider(CrawlSpider):
    name = 'SinaBlog1'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/blog_5af303e30102yb5x.html']

    #articleLink = LinkExtractor(restrict_xpaths=('//div[@class="articalfrontback SG_j_linedot1 clearfix"]/div/a'))
    #articleLink = LinkExtractor(restrict_css=('div[class="articalfrontback SG_j_linedot1 clearfix"] > div > a'))
    articleLink = LinkExtractor(allow=('/s/blog_.*?\.html'))

    rules = [
        Rule(articleLink,callback='parse_item',follow=True)
    ]

    def parse_item(self, response):
        item = BlogcrwalspiderItem()
        item['title'] = response.xpath('//h2[@class="titName SG_txta"]/text()').extract()
        if len(item['title'])>0:
            item['title'] = item['title'][0]
        else:
            item['title'] = '空'
        item['url'] = response.url

        # temps = response.xpath('//div[@class="IL"]/span').extract()
        # print('temps len:',len(temps))
        # if len(temps)>0:
        #     item['vnums'] = temps[0].xpath('./text()')[0]
        #     item['cnums'] = temps[1].xpath('./text()')[0]
        # item['snums'] = response.xpath('//a[@class="zznum"]/text()').extract()[0]
        yield item
