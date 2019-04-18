# -*- coding: utf-8 -*-
import scrapy


class Renren3Spider(scrapy.Spider):
    name = 'renren3'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/966924492']
    strcookies = 'anonymid=jru48ifmt3j3si; _r01_=1; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1549513361097%7C1%7C1551858470234; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1553336590; _de=32B20555AD3784A6BF2D3D01B72FE013; depovince=HEN; ick_login=33d63d3d-33f7-4226-962b-b6cd3bbbc525; jebecookies=d82bebfc-5e5c-4b96-a517-82f60f8e37d4|||||; p=3d97ce40b39502fb09afbef4deccb41d2; first_login_flag=1; t=6bf0bf89e9340e37fe740fd5ca0fe56a2; societyguester=6bf0bf89e9340e37fe740fd5ca0fe56a2; id=966924492; xnsid=ff381b2d; ver=7.0; loginfrom=null; JSESSIONID=abc3PqfdiuzKd5zt_XaOw; jebe_key=757177d7-4364-40db-be6b-cdd5b17c1d81%7C077a3e2b1c00096d5c13732ceee74ce5%7C1554791263698%7C1%7C1554791263503; wp_fold=0'
    cookies = {item.split('=')[0]:item.split('=')[1] for item in strcookies.split(';')}

    # 可以重写Spider类的start_requests方法，附带Cookie值，发送POST请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_page)

    # 处理响应内容
    def parse_page(self, response):
        print("===========" + response.url)
        with open("./data/page_3.html", "w", encoding='utf-8') as filename:
            filename.write(response.body.decode('utf-8'))
