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
        # 提取每个页面中帖子的链接
        links = response.xpath("//a[@class='news14']/@href").extract()
        print('len:',len(links))
        # 遍历，请求详情页面
        for link in links:
            yield scrapy.Request(link,callback=self.parse_item)

        # 设置页码终止的条件
        if self.offset < 30000:
            self.offset += 30
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)


    def parse_item(self,response):
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
