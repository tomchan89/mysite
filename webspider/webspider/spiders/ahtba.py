# -*- coding: utf-8 -*-
import scrapy


class AhtbaSpider(scrapy.Spider):
    name = 'ahtba' #爬虫名
    allowed_domains = ['qq.com']  #爬取范围
    #start_urls = ['https://www.qq.com']
    start_urls = ['http://www.ahtba.org.cn/Notice/AnhuiNoticeSearch?spid=714&scid=597&srcode=341800&sttype=&stime=365&stitle=&sCompanyName=&isPageBarSearch=1&pageNum=1&pageSize=15'] #爬取根地址

    def parse(self, response):
        xc_list = response.xpath("//div[@class='iweifa_right_nr']//p")
        print('*'*20)
        #iweifas= response.xpath("//div[@class='layout qq-footer']/a")
        print(type(xc_list))
        print(len(xc_list))
        # for iweifa in iweifas:
        #     ann = iweifa.xpath(".//text()").get()
        #     if ann is not None:
        #        print(ann)
        print('*' * 20)
