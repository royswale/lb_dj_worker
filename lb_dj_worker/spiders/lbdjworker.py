# -*- coding: utf-8 -*-
import scrapy


class LbdjworkerSpider(scrapy.Spider):
    name = 'lbdjworker'
    allowed_domains = ['lb-dj.com']
    start_urls = ['http://lb-dj.com/']

    def parse(self, response):
        pass
