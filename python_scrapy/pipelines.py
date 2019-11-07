# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from python_scrapy.items import txItem


#先执行
class PythonScrapyPipeline(object):
    def process_item(self, item, spider):
        if(spider.name == 'itcast'):
            print(item)
            item['hh'] = 'aaa'
        return item

#依次执行(item 是上一个的 item)
class PythonScrapyPipelineHuaban(object):
    def process_item(self, item, spider):
        if(spider.name == 'huaban'):
            print(item)
        return item

#依次执行(item 是上一个的 item)
class PythonScrapyPipelineTX(object):
    def process_item(self, item, spider):
        #几种判断方法都行 
        # if isinstance(item,txItem):
        if(spider.name == 'tx'):
            item = dict(item)
            print(item)
        
        with open('resource/tx.txt','a') as file_obj:   
            file_obj.write(item["name"]+'\n')

        return item