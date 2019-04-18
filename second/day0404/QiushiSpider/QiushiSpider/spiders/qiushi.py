# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
"导入链接提取器"
from scrapy.linkextractors import LinkExtractor
# from SunSpider.items import SunspiderItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    "匹配翻页"
    pagelink = LinkExtractor(restrict_xpaths=('//span[@class="next"]',))
    # "匹配每个帖子的链接"
    # contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]',))
    "不需要有回调函数,parse_item详情内容的回调函数"
    rules = [
        Rule(pagelink, callback='parse_item', follow=True),
        # Rule(contentlink, callback='parse_item')
    ]

    def parse_item(self, response):
        "爬取封面图片，标题，作者，点赞数，品论述"
        ls = response.xpath('//div[@class="recommend-article"]//li')
        print(ls)
