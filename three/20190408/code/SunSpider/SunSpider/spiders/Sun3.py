# -*- coding: utf-8 -*-
''' 实现自动化爬取'''
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from SunSpider.items import SunspiderItem


class Sun3Spider(CrawlSpider):
    name = 'Sun3'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    # 匹配翻页
    pagelink = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]',))
    # 匹配每个帖子的链接
    contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]',))
    rules = [
        Rule(pagelink,follow=True),
        Rule(contentlink,callback='parse_item')
    ]


    def parse_item(self,response):
        print('url:',response.url)
        item = SunspiderItem()
        # 标题
        item['name'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()').extract()[0]
        # 编号
        item['number'] = response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[2]/text()').extract()[0].strip().split(':')[-1]
        # 编号
        item['url'] = response.url
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//td[@class="txt16_3"]//text()').extract()
        item['content'] = ''.join(item['content']).strip()

        tmp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].strip().split(' ')
        item['author'] = tmp[0].split('：')[-1]
        item['pub_date'] = tmp[1].split('：')[-1] + ' '+ tmp[2]

        yield item
