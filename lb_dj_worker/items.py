# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LbDjWorkerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    serviceType = scrapy.Field()
    mainCategory = scrapy.Field()
    deputyCategory = scrapy.Field()
    workerNick = scrapy.Field()
    coreMargin = scrapy.Field()
    depositLevel = scrapy.Field()
    isRealnameAuth = scrapy.Field()
    receiveCount = scrapy.Field()
    workerImage = scrapy.Field()
    selfEvaluation = scrapy.Field()
    starLevel = scrapy.Field()
    evaluationScore = scrapy.Field()
    creditScore = scrapy.Field()
    certificationName = scrapy.Field()
    creditLevel = scrapy.Field()
    creditDescription = scrapy.Field()

    pass
