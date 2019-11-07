# -*- coding: utf-8 -*-
import scrapy


class HuabanSpider(scrapy.Spider):
    name = 'huaban'
    allowed_domains = ['https://huaban.com']
    start_urls = ['https://huaban.com/']

    def parse(self, response):
        item = {}
        item["name"] = 'huaban'
        yield item
        pass
