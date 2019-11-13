# -*- coding: utf-8 -*-
import scrapy
import re

class HuabanSpider(scrapy.Spider):
    name = 'huaban'
    allowed_domains = ['huaban.com']
    # start_urls = ['https://huaban.com/boards/38063122/']
    start_urls = ['https://huaban.com/boards/30643621/?k2sahp69&max=1182250553&limit=20&wfl=1']


    def parse(self, response):
        cookies = "referer=http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8yXrlf1eS1B_QGXqV6uxuN_hA0XH3U4hE-SljVgdVxi%26wd%3D%26eqid%3Dbc720428001529cf000000025dc76094; sid=a89kBZ8espvxPsXHgpIbrHnvG4P.m6h0bQA3PlA0s%2BvF%2BaDxckx3RFrIwUKgdKxLvQYMf%2BQ; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAAFh0lEQVRYR8WXCWxUVRSGv9PSDRAMEJaWHa1RkEbgDZvSV424kYBKSDBRtrBIFaW4IQEEAqgEaFEIJkhdohUEXIg0sjhTCgIzBUUBDQINBaHSWiJWaCkzx9yZ12FKWVpT4k0m82bmLuc75z%2F%2FeyOoKs6YvnAhHYuKSF%2B%2BnEBUVPBbFRkIfA20F6ionlvXd4U5QCOBGXVdc7V5mWWZ4Tiv9rtEgkxauZIOJ04wY%2F788FwV6QFsAToI%2BOsbjMIkoLXA3PqujZxfb5Dkw4eZtngx0X4%2F%2FuhoUxkL%2BAS4C7gHGAasAloCjwMfCBxRaARMBlxAEbBGYL%2FCWGC5s0dP4CWB7cFqwxBgBHAK2CewVqEd8L6jgleAj4B5WWWZl66XiBoVGbt6NcvT01k6dWp4zfSFCw1EMtAfCAA%2FANMEtjmy2QV8C%2BQAnwIbgXzgdROwU5FkgQyFAcBOoBtgA3cCrwIvAK2M%2FBTmGVhgEPAHcBRIyirLNNfXHDVAJq9YQavSUubOmhUpLQORZ6TlgGwD3nCCnAIcBLxO8L0EAgqjgWYCyzRUpSQnSAHcJsPATFNRgbMaStQKYDDQxNmrt3Oe6c9x9QIZk50dbPY5s2dHgnQH1gPm3TScD3hOYLdCJEgh0EngH4X3gN9NXzggJtvm2oCY9RmEeuZ5gZ8VhgJvOmcYiW4GHogAeSarLLOsThXpdvQoKyZPJq6ykpE5OZxu1y54XREfb8r%2BFvCQIwvjBEbrucAywADc62TZ9NAaJ6hyoB%2BQ6gR9vyPPcYQk9gTwITAdWOoEORK46PRTH0Iu%2Bb1TESPZG0urS2EhMVVVwSavjIvjWNeuxFdUcCEhIQU4ZzQM%2FAQYX37YaehioKkDY5qxr3O4kZuRhsl%2BIpDgmMVfwPZq99NQlc2%2BO5z5R4wMgQuEHNK84ox9Z5VlHqoTyLVRxcjhfx%2F1st%2BrRiu1QdS9uz0SvQalCiEGOCK2NUo93o0gLUIVkGyx%2B7xTvafmF3TEHzC91hiJmi%2BpfYzD1Rih9SSj5Eqa68Ur7yOiMPzY3exqU8TJpqa4l0cN16oriJmnHu8YkFWge8R2Gc2jbncjpOkp0C%2FFdk0IQ4S%2BP46wAZUNEPjG9I7YLiO94FC3dysit6CtUpHSItB3xXaFb6LrirL1kaJkGl%2BKZVOnX%2Fmt%2BZ8NA%2BLA7ALpRUxsBxmYckbz9%2FbG799Cgt4uffuGT9I8XzrKEjShpaT1KFeP1wtSKrb1aHCfgoLmlGsJMFRsK1c9XgMwUWxXm%2BpofQe%2F0PONqrBK2uNJPMbhW0sbEMTtG47wObBEbGuaenwfA23Fth6MPEU9vrdRptA4kGQA1eM1TtRWbFfXUEIK0kC3EsUIGWSt1zzvPAJMJzYu0STIzDE9YqQ18VBfvks62rAgoSB8x4EYsa1EdXtPIjLeZLUmiDcXpLvYVsfLlaSF2K47gp%2FzvNMIGIsPdJa0fieDIMprJGjb6soakOhAFON%2FsW4SSPBQMU%2B2i1CelDTrtlpNfEWGnYq0DIMYSV7y7yGKpyTVtTYMEhOXFFmRmwviLoyH0mKE5sACsa1aj%2BsalKDmVGdY3d4fgQPExmVwqaIJgdankZKzqIyRNOszdXszQYaYpKhn731i986vltaEQy42dzhCYbOaN%2Fr%2F7Fo1pOP2rQMdFqnpWlVx%2B3YjGo3IDgKMITY2mYuVmxBSDCDnZSbC04jMQnURwmhUzN3dPEA%2BltVz56YBxZ3ocyaJU03%2B5qvOh6iKvvyvomFA8velEPBPklTr2ataeLXFenzLQLsQEzcu6HJ5BaNQTRLbWuA0fQYaGGxsXdKsderZ0x%2BJGkGg%2FOWslP1VvUoSgw97Cf4YDrQo5lxsZfi4BgG5XvAN9dtNubM3VHD12edGIP8C7CaAN6TZWBQAAAAASUVORK5CYII%3D%2CMacIntel.1600.900.24; BAIDU_SSP_lcr=http://www.baidu.com/link?url=8yXrlf1eS1B_QGXqV6uxuN_hA0XH3U4hE-SljVgdVxi&wd=&eqid=bc720428001529cf000000025dc76094; _uab_collina=157334747750990448741151; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1573347478; UM_distinctid=16e52d149542eb-04ba8366965736-36637903-15f900-16e52d149562f8; CNZZDATA1256903590=1631204072-1573345097-null%7C1573345097; __asc=841c505716e52d14a41885609f3; __auc=841c505716e52d14a41885609f3; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; uid=19035743; _tskw=1; _cnzz_CV1256903590=is-logon%7Clogged-in%7C1573347508890%26urlname%7Clyl937373211%7C1573347508890; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1573347508"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )
    def parse(self, response):
        print(re.findall("心忆星空",response.body.decode()))
        with open("resource/a.html","w",encoding="utf-8") as f:
                    f.write(response.body.decode())
     


        # yield scrapy.Request(
        #     "详情页",
        #     callback=self.parse_detial
        # )

    # def parse_detial(self,response):
    #     print(re.findall("aaa",response.body.decode()))