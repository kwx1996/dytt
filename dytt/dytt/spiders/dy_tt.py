# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import DyttItem

class DyTtSpider(scrapy.Spider):
    name = 'dy_tt'
    # allowed_domains = ['https://www.dygod.net/html/gndy/oumei/index_{}.html']
    start_urls = ['https://www.dygod.net/html/gndy/oumei/index_1.html/']

    def parse(self, response):
        th = response.xpath('//div[@class="co_area2"]//div[@class="co_content8"]//ul//table')
        for i in range(len(th)):
            name = th[i].xpath('.//td[2]/b//a[2]/@title')[0].extract()
            item = DyttItem()
            item['name'] = name

            yield item
        for i in range(3, 214):
            yield Request(url='https://www.dygod.net/html/gndy/oumei/index_{}.html'.format(i), callback=self.parse)
