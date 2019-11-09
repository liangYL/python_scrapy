# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'js'
    # allowed_domains = ['www.lagou.com']
    # start_urls = ['https://www.lagou.com/']
    allowed_domains = ["jianshu.com"]
    start_urls = ['https://www.jianshu.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.*jianshu.com/u/*.'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # link = LinkExtractor(allow=r'.*jianshu.com/u/*.')
        # links = link.extract_links(response)
        # print(links)
        
        print(response.xpath("//ul[@calss='trigger-menu']"))
        print(response.xpath("//div[@id='list-container']/ul"))
        print(response.xpath('//div[@calss="main-top"]'))

        for li in response.xpath("//div[@id='list-container']/ul"):
            imgstr = li.xpath(".//img/@src").extract_first()

            with open('resource/jianshu.html','a') as file_obj:   
                if imgstr.startswith('http'):
                    file_obj.write("<img src="+str(imgstr)+">" +'\n')
                else:   
                    file_obj.write("<img src="+ 'https:'+str(imgstr)+">" +'\n')

        for each in response.xpath("//ul[@class='trigger-menu']"):
            
            print(each.xpath("./li/a/text()").extract_first())



 