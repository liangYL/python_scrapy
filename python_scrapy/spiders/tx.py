# -*- coding: utf-8 -*-
import scrapy
from python_scrapy.items import txItem

class TxSpider(scrapy.Spider):
    name = 'tx'
    allowed_domains = ['99mi.com']
    start_urls = ['http://www.99mi.com/article_cat-19-1.html']

    def parse(self, response):
   
        res = response.xpath("//ul[@class='new-list']/li")
      
        for li in res:
            item = txItem()
            item['name'] =  li.xpath("./p/text()").extract_first()
            item['date'] =  li.xpath("./h2/text()").extract_first()
            yield item

        next_url = response.xpath("//div[@class='pagebar']/a[@class='next']/@href").extract_first()
        
        if next_url:
            next_url = "http://www.99mi.com/" + next_url
            print(next_url)
            yield scrapy.Request(
                    next_url,
                    callback=self.parse 
                  )