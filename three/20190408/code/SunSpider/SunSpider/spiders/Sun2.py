# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem

class Sun2Spider(scrapy.Spider):
    name = 'Sun2'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url]


    def parse(self, response):
        ls = response.xpath('//div[@id="morelist"]/div/table[2]//table//tr')
        print('len:',len(ls))
        for each in ls:
            item = SunspiderItem()
            item['name'] = each.xpath('./td[2]/a[2]/text()').extract()[0]
            item['url'] = each.xpath('./td[2]/a[2]/@href').extract()[0]
            item['number'] = each.xpath('./td[1]/text()').extract()[0]
            item['author'] = each.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = each.xpath('./td[5]/text()').extract()[0]

            req = scrapy.Request(item['url'], callback=self.parse_item)
            req.meta['item'] = item
            yield req

        # 设置页码终止的条件
        if self.offset < 30000:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


    def parse_item(self,response):
        item = response.meta['item']
        # 内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//td[@class="txt16_3"]//text()').extract()
        item['content'] = ''.join(item['content']).strip()

        yield item