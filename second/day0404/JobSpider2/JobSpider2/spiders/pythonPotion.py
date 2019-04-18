# -*- coding: utf-8 -*-
import scrapy
import re
from JobSpider2.items import Jobspider2Item


class PythonpotionSpider(scrapy.Spider):
    name = 'pythonPotion'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?keywords=&tid=0&start=0#a']

    def __init__(self):
        self.str1 = 'https://hr.tencent.com/position.php?keywords=&tid=0&start='
        self.str2 = '#a'
        self.startpage = 1
        self.endpage = 312

    def get_url(self):
        return self.str1 + str(self.startpage) + self.str2

    def parse(self, response):
        # print(response.body)
        job_list = response.xpath('//table[@class="tablelist"]//tr')
        job_list.pop(0)
        job_list.pop()
        print(len(job_list))
        for item in job_list:
            position = item.xpath('./td[1]/a/text()').extract()[0].strip()
            print("职位：", position)
            category = item.xpath('./td[2]/text()')
            if len(category) > 0:
                Job_category = category.extract()[0].strip()
                print("职位类别：", Job_category)
            people_number = item.xpath('./td[3]/text()').extract()[0].strip()
            print("人数- ：", people_number)
            site = item.xpath('./td[4]/text()').extract()[0].strip()
            print("地点：", site)
            time = item.xpath('./td[5]/text()').extract()[0].strip()
            print("时间：", time)

            item = Jobspider2Item()
            item['position'] = position
            item['Job_category'] = Job_category
            item['people_number'] = people_number
            item['site'] = site
            item['time'] = time
            yield item
            print("="*60)

        print(response.url)
        print(self.str1)
        p = 'start=' + r'(\d+)'
        cur_page = re.search(p, response.url).group(1)
        print("当前页码：", cur_page)
        self.startpage = int(cur_page) + 10
        if self.startpage < self.endpage*10:
            url = self.get_url()
            yield scrapy.Request(url, callback=self.parse)

