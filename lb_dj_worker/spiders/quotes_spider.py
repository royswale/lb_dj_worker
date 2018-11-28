import scrapy
import json

from lb_dj_worker.items import LbDjWorkerItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        # urls = [
            # 'https://www.lb-dj.com/website/worker/workerListNew?city=&province=&district=&category=&codeType=&thisPage=1',
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        # ]
        url = 'https://www.lb-dj.com/website/worker/workerListNew?city=&province=&district=&category=&codeType=&thisPage='
        for i in range(1, 7830):
            yield scrapy.Request(url=url+str(i), callback=self.parse)

    def parse(self, response):
        data = response.body
        # data = data.decode('utf-8')
        # data = data.decode('unicode-escape')
        data = json.loads(data)
        # self.log(data)
        # self.log( json.dumps(data, sort_keys=True, indent = 4, separators = (',', ': '), ensure_ascii=False) )
        # countpage = data['countPage']
        # self.log(countpage)
        list = data['list']
        for i in list:
            item = LbDjWorkerItem()

            item['id'] = i['id']
            item['serviceType'] = i['serviceType']
            item['mainCategory'] = i['mainCategory']
            item['deputyCategory'] = i['deputyCategory']
            item['workerNick'] = i['workerNick']
            item['coreMargin'] = i['coreMargin']
            item['depositLevel'] = i['depositLevel']
            item['isRealnameAuth'] = i['isRealnameAuth']
            item['receiveCount'] = i['receiveCount']
            item['workerImage'] = i['workerImage']
            item['selfEvaluation'] = i['selfEvaluation']
            item['starLevel'] = i['starLevel']
            item['evaluationScore'] = i['evaluationScore']
            item['creditScore'] = i['creditScore']
            item['certificationName'] = i['certificationName']
            item['creditLevel'] = i['creditLevel']
            item['creditDescription'] = i['creditDescription']

            yield item




    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)
