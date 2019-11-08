# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class wmtItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    p_id = scrapy.Field()
    content = scrapy.Field()

# class huabanItem(scrapy.Item):
    # name = scrapy.Field()
    # date = scrapy.Field()