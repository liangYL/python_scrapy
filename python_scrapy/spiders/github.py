# -*- coding: utf-8 -*-
import scrapy
import re


# 方法一 手动拼接 post 参数 登录

# class GithubSpider(scrapy.Spider):
#     name = 'github'
#     allowed_domains = ['github.com']
#     start_urls = ['https://github.com/login']

#     def parse(self, response):
#         authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
#         utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
#         ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()
#         # webauthn-support = response.xpath("//div[@calss='auth-form-body mt-3']/input[@name='webauthn-support']/@value").extract_first()
#         # webauthn-iuvpaa-support = response.xpath("//div[@calss='auth-form-body mt-3']/input[@name='webauthn-iuvpaa-support']/@value").extract_first()
#         commit = response.xpath("//input[@name='commit']/@value").extract_first()
#         timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
#         timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()

#         post_data = {
#             "login":"757228500@qq.com",
#             "password":"xxx",
#             "authenticity_token":authenticity_token,
#             "utf8":utf8,
#             "commit":commit,
#             "ga_id":ga_id,
#             "webauthn-support":response.xpath("//input[@name='webauthn-support']/@value").extract_first(),
#             "webauthn-iuvpaa-support":response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").extract_first(),
#             "required_field_48c3":'' ,
#             "timestamp": timestamp,
#             "timestamp_secret":timestamp_secret,
#         }
 
#         yield scrapy.FormRequest(
#             "https://github.com/session",
#             formdata=post_data,
#             callback=self.after_login
#         )

#     def after_login(self,response):
#         print(re.findall("liangYL|liangyl",response.body.decode()))
#         with open("resource/b.html","w",encoding="utf-8") as f:
#                     f.write(response.body.decode())
#         res = response.xpath("//ul[@class='list-style-none']")
#         for sss in res:
#                 ttt = sss.xpath('./li')
#                 for a in ttt:
#                     print(a.xpath('./div/a/@href').extract_first())



# 方法二 自动获取 from 数据 登录

class Github2Spider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, #自动的从response中寻找from表单
            formdata={"login":"757228500@qq.com","password":"xxx"},
            callback = self.after_login
        )

    def after_login(self,response):
        print(re.findall("liangYL|liangyl",response.body.decode()))
        with open("resource/b.html","w",encoding="utf-8") as f:
                    f.write(response.body.decode())
        res = response.xpath("//ul[@class='list-style-none']")
        for sss in res:
                ttt = sss.xpath('./li')
                for a in ttt:
                    print(a.xpath('./div/a/@href').extract_first())



# 方法三 不登录用cookies获取

# class RenrenSpider(scrapy.Spider):
#     name = 'gh'
#     allowed_domains = ['renren.com']
#     start_urls = ['http://www.renren.com/327550029/profile']

#     def start_requests(self):
#         cookies = "anonymid=jcokuqturos8ql; depovince=GW; jebecookies=f90c9e96-78d7-4f74-b1c8-b6448492995b|||||; _r01_=1; JSESSIONID=abcx4tkKLbB1-hVwvcyew; ick_login=ff436c18-ec61-4d65-8c56-a7962af397f4; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=90dea4bfc79ef80402417810c0de60989; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; t=24ee96e2e2301bf2c350d7102956540a9; societyguester=24ee96e2e2301bf2c350d7102956540a9; id=327550029; xnsid=e7f66e0b; loginfrom=syshome; ch_id=10016"
#         cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
#         yield scrapy.Request(
#             self.start_urls[0],
#             callback=self.parse,
#             cookies=cookies
#         )

#     def parse(self, response):
#         print(re.findall("张三",response.body.decode()))
#         yield scrapy.Request(
#             "http://www.renren.com/327550029/profile?v=info_timeline",
#             callback=self.parse_detial
#         )

#     def parse_detial(self,response):
#         print(re.findall("张三",response.body.decode()))