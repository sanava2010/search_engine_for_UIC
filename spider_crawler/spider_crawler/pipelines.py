# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class SpiderCrawlerPipeline(object):
    # def __init__(self):
    #     self.create_connection()
    #     self.create_table()

    # def create_connection(self):
    #     self.conn=sqlite3.connect('uic.db')
    #     self.curr=self.conn.cursor()
    
    # def create_table(self):
    #     self.curr.execute(""" DROP TABLE IF EXISTS uic""")
    #     self.curr.execute("""create table uic(url text, content text)""")

    # def process_item(self, item, spider):
    #     self.store_db(item)
    #     print("Pipeline:"+item['url'])
    #     return item
    
    # def store_db(self,item):
    #     self.curr.execute(""" insert into uic values (?,?)""",(item['url'],item['content']) )
    #     self.conn.commit()
    pass
