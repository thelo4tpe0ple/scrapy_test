from typing import Any
import scrapy
from scrapy.http import Response
from ..items import MayiwxItem
from selenium.webdriver.chrome.options import Options
import time
class MayiSpider(scrapy.Spider):
    name = "mayi"
    allowed_domains = ["www.mayiwxw.com"]
    num = 3302
    page = 107
    start_urls = ["https://www.mayiwxw.com/0_10/"+str(19960+page)+".html"]
    
    
    def parse(self, response):
        items = MayiwxItem()
        options = Options()
        options.add_argument('--headless')
        
        items['title'] = response.xpath('//div[@class = "bookname"]/h1/text()').get()
        contents = response.xpath('//*[@id="content"]/text()').extract()
        res = ""
        for content in contents:
            tmp = content.replace("\n","").replace("\xa0","")
            res+=tmp
        items['content']=res
        #print(response.text)
        yield items
        if self.page <=self.num:
            self.page+=1
            yield scrapy.Request("https://www.mayiwxw.com/0_10/{}.html".format(19960+self.page),callback=self.parse)

        
