# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql

class LbDjWorkerPipeline(object):

    def open_spider(self, spider):
        self.file = open('items1.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # self.log('Found a worker whose nickname is %s.' % item['nick'])
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


class MySQLPipeline(object):

    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME', 'scrapy_db')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'root')

        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        # self.db_conn = pymysql.connect('127.0.0.1', 3306, 'scrapy_db', 'root', 'root', 'utf8')
        self.db_cursor = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            # int(item['id']),
            item['id'],
            item['serviceType'],
            item['mainCategory'],
            item['deputyCategory'],
            item['workerNick'],
            item['coreMargin'],
            item['depositLevel'],
            item['isRealnameAuth'],
            item['receiveCount'],
            item['workerImage'],
            item['selfEvaluation'],
            item['starLevel'],
            item['evaluationScore'],
            item['creditScore'],
            item['certificationName'],
            item['creditLevel'],
            item['creditDescription'],
        )

        sql = 'INSERT INTO workers VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # sql = 'INSERT INTO workers VALUES(%s)'
        self.db_cursor.execute(sql, values)