# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        res = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(res)
        for r in res:
            item = {}
            item["name"] = r
            #不能数组,可字典,none,baseitem,requst
            yield item
 