#-*- encoding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import log
import MySQLdb
from twisted.enterprise import adbapi


class LaozhaocrawlPipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect(user="root",db="blogcrawl",passwd="123456",host="localhost",charset="utf8",use_unicode=True)
        self.cursor=self.conn.cursor()
        if self.cursor:
        # self.dbpool=adbapi.ConnectionPool('MySQLdb',
        #                                   db='blogcrawl',
        #                                   user='root',
        #                                   passwd='123456',
        #                                   cursorclass=MySQLdb.cursors.DictCursor,
        #                                   charset="utf-8",
        #                                   use_unicode=False)
            print "*****************************************************"

    def process_item(self, item, spider):
        try:
            # print "__________________________________________________"+item['tags'][0].encode('utf-8')
            self.cursor.execute("""
            insert into blog (title,content,categories,tags,link)
            values (%s,%s,%s,%s,%s)
            """,
                            (item['title'].encode("utf-8"),
                item['content'].encode("utf-8"),
                item['categories'].encode("utf-8"),
                item['tags'].encode("utf-8"),
                item['link'].encode("utf-8") )
            )
            self.conn.commit()
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

