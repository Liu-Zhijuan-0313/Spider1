# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem


class Sun1Spider(scrapy.Spider):
    name = 'Sun1'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url]

    def parse(self, response):

        "提取页面中每个帖子的链接"
        links = response.xpath('//a[@class="news14"]/@href').extract()
        print(len(links))

        "遍历，请求详情页面"
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)

        "设置页码终止的条件"
        if self.offset < 30000:
            self.offset += 30
            yield scrapy.Request(self.url+str(self.offset), callback=self.parse)

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
        pub_time = test[1].split("：")[1] + " " +test[2]
        print("发布时间：", pub_time)

        item = SunspiderItem()
        item['name'] = name
        item['num'] = num
        item['link'] = link
        item['content'] = content
        item['author'] = author
        item['pub_time'] = pub_time
        yield item

