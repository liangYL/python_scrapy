# -*- coding: utf-8 -*-
import scrapy
from python_scrapy.items import wmtItem

class WmtSpider(scrapy.Spider):
    name = 'wmt'
    allowed_domains = ['99mi.com']
    start_urls = ['http://www.99mi.com/article_cat-35-1.html']
    # 详情
    # http://www.99mi.com/article_cat.php?id=17&art_id=1106

    def parse(self, response):
   
        res = response.xpath("//ul[@class='new-list']/li")
        resid = response.xpath("//ul[@class='new-class']/li[@class='this']/a/@href").extract_first()

        for li in res:
            item = wmtItem()
            item['name'] =  li.xpath("./p/text()").extract_first()
            item['date'] =  li.xpath("./h2/text()").extract_first()

            str1 = "(";
            str2 = ")";
            cli = li.xpath("./i/@onclick").extract_first()
            cli = cli[cli.index(str1)+1:cli.index(str2)]
            # cli = cli[8:-1]   #和上面等价
            item['url'] = 'http://www.99mi.com/article_cat.php?id=' + resid[resid.index('=')+1:]+ '&art_id=' + cli

            yield item

        next_url = response.xpath("//div[@class='pagebar']/a[@class='next']/@href").extract_first()
        
        if next_url:
            next_url = "http://www.99mi.com/" + next_url
            print(next_url)
            yield scrapy.Request(
                    next_url,
                    callback=self.parse 
                  )