# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import re
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# from  selenium.webdriver.chrome.options import Options    # 使用无头浏览器(无浏览器界面后台运行)


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://blog.csdn.net']
    header = {
        ":path": "/v1/register/pc/login/doLogin",
        "referer": "https://passport.csdn.net/login",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    def start_requests(self):
        return [scrapy.Request(         
            url="https://passport.csdn.net/login",
            callback=self.parseLogin,
            headers=self.header
        )] 
    def parseLogin(self, response):
        # chorme_options = Options()
        # chorme_options.add_argument("--headless")
        # chorme_options.add_argument("--disable-gpu")
        # dri = webdriver.Chrome(chrome_options=chorme_options)
        dri = webdriver.Chrome()
        dri.get("https://passport.csdn.net/login")
        aa =  dri.find_element_by_link_text("账号登录")
        aa.click()
        dri.find_element_by_id('all').send_keys('xxx')
        sleep(1)
        dri.find_element_by_id('password-number').send_keys('xxx')
        sleep(1)
        # js = "document.getElementByClass('btn-primary__disabled').style.display='block'"
        # dri.execute_script(js) //执行 js
        # bb = dri.find_element_by_xpath("//input[@id='kw']") //xpath 模式查找

        bb =  dri.find_element_by_class_name('btn-primary')
        bb.click()

        #滑动验证
        button = dri.find_element_by_id('nc_1_n1z')    # 找到“蓝色滑块”
        action = ActionChains(dri)            # 实例化一个action对象
        action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
        action.reset_actions()
        action.move_by_offset(780, 0).perform()  # 移动滑块
        # action.drag_and_drop_by_offset(button, 700, 0).perform()

        cookie_items = dri.get_cookies()  
        cookie_dict = {}
        for item_cookie in cookie_items:
            cookie_dict[item_cookie["name"]] = item_cookie["value"]
        dri.close()  # 关闭浏览器
        return [scrapy.Request(
            url="https://download.csdn.net/my/downloads",
            cookies=cookie_dict,
            headers=self.header
        )] 
    def parse(self, response):
        print(re.findall("iOS_leungYL",response.body.decode()))
