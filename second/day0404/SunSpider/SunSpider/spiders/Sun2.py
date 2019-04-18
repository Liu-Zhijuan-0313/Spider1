# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem


class Sun2Spider(scrapy.Spider):
    name = 'Sun2'
    allowed_domains = ['sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url]

    def parse(self, response):
        ls = response.xpath('//div[@class="greyframe"]/table[2]//table//tr')
        print(len(ls))
        for each in ls:
            num = each.xpath('./td[1]/text()').extract()[0]
            print("编号：", num)
            name = each.xpath('./td[2]/a[2]/text()').extract()[0]
            print("标题：", name)
            link = each.xpath('./td[2]/a[2]/@href').extract()[0]
            print("链接：", link)
            author = each.xpath('./td[4]/text()').extract()[0]
            print("作者：", author)
            pub_time = each.xpath('./td[5]/text()').extract()[0]
            print("发布时间：", pub_time)
            print("="*60)

            item = SunspiderItem()
            item['name'] = name
            item['num'] = num
            item['link'] = link
            item['author'] = author
            item['pub_time'] = pub_time
            yield item
            """
            meta是一个字典，主要是用解析函数之间传递值，
            常见的情况是：在parse中给item某些字段提取了值，但是另外一些值需要在parse2中提取，
            这时候需要将parse中的item传到parse2方法中处理，显然无法直接给parse2设置而外参数。 
            Request对象接受一个meta参数，一个字典对象，同时Response对象有一个meta属性可以取到相应request传过来的meta。
            """
            req = scrapy.Request(link, callback=self.parse_item)
            req.meta['item'] = item
            yield req

            "设置页码终止的条件"
            if self.offset < 30000:
                self.offset += 30
                yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        item = response.meta['item']
        "内容"
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/text()').extract()
        item['content'] = ''.join(item['content']).strip()
        yield item
