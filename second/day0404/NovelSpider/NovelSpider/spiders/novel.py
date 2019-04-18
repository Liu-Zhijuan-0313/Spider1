# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
"导入链接提取器"
from scrapy.linkextractors import LinkExtractor
from NovelSpider.items import NovelspiderItem


class NovelSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['www.quanben.net']
    start_urls = ['https://www.quanben.net/modules/article/articlelist.php?fullflag=1&page=1']

    "匹配翻页"
    pagelink = LinkExtractor(restrict_xpaths=('//a[@class="next"]',))
    "匹配每个帖子的链接"
    # contentlink = LinkExtractor(restrict_xpaths=('//ul[@class="item-con"]/li/span/a/@href',))
    "不需要有回调函数,parse_item详情内容的回调函数"
    rules = [
        Rule(pagelink, callback='parse_item', follow=True)
        # Rule(contentlink, callback='parse_item')
    ]

    def parse_item(self, response):
        ls = response.xpath('//ul[@class="item-con"]/li')
        for item in ls:
            "爬取小说名称，url，类别，作者，更新时间，状态"
            name = item.xpath('./span[2]/a/text()').extract()
            print("小说名：", name)
            url = item.xpath('./span[2]/a/@href').extract()
            print("链接：", url)
            leibie = item.xpath('./span[1]/text()').extract()
            print("类别：", leibie)
            author = item.xpath('./span[3]/text()').extract()
            print("作者：", author)
            pub_time = item.xpath('./span[4]/text()').extract()
            print("更新时间：", pub_time)
            status = item.xpath('./span[5]/text()').extract()
            print("状态：", status)

            item = NovelspiderItem()
            item['name'] = name
            item['url'] = url
            item['leibie'] = leibie
            item['author'] = author
            item['pub_time'] = pub_time
            item['status'] = status
            yield item
