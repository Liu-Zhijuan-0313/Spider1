# -*- coding: utf-8 -*-
"""
实现自动化爬取
"""
import scrapy
from scrapy.spiders import CrawlSpider, Rule
"导入链接提取器"
from scrapy.linkextractors import LinkExtractor
from SunSpider.items import SunspiderItem


class Sun3Spider(CrawlSpider):
    name = 'Sun3'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    start_urls = [url]
    "匹配翻页"
    pagelink = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]',))
    "匹配每个帖子的链接"
    contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]',))
    "不需要有回调函数,parse_item详情内容的回调函数"
    rules = [
        Rule(pagelink, follow=True),
        Rule(contentlink, callback='parse_item')
    ]

    "数据提取函数名不能用parse，因为父类用过此名字"
    def parse_item(self, response):
        name = response.xpath('//div[@class="wzy1"]//span[@class="niae2_top"]/text()').extract()[0]
        print("标题：", name)
        num = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[2]/text()').extract()[0].strip()
        print("编号：", num)
        link = response.url
        print("链接：", link)

        content = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/text()').extract()
        content = ''.join(content).strip()
        # content = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/text()').extract()[0].strip()
        print("内容：", content)

        test = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].split(" ")
        author = test[0].split("：")[1]
        print("作者：", author)
        pub_time = test[1].split("：")[1] + " " + test[2]
        print("发布时间：", pub_time)

        item = SunspiderItem()
        item['name'] = name
        item['num'] = num
        item['link'] = link
        item['content'] = content
        item['author'] = author
        item['pub_time'] = pub_time
        yield item
