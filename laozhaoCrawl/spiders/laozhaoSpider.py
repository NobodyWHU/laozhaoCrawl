#-*- encoding:utf-8 -*-

__author__ = 'No_Body'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request,Response,HtmlResponse
import urlparse
import codecs
import re
from laozhaoCrawl.items import *

fp=codecs.open("chenhaoresult.txt",'w','utf-8')
class laozhaoSpider(BaseSpider):
    name="laozhao"
    allowed_domains = ['blog.zhaojie.me']
    start_urls=['http://blog.zhaojie.me']


    def parse(self, response):
        """

        :param response:
        """
        hxs=HtmlXPathSelector(response)
        page=hxs.select("//div[@id='pager']/span[@class='current']/text()").extract()[0]
        next_page=int(page)+1

        for per in hxs.select("//div[@class='post']"):
            partlink=per.select("div[@class='entry']/a/@href").extract()[0]
            link=urlparse.urljoin(response.url,partlink)
            yield Request(link, callback=self.parse_blog)

        if next_page<=31:
            url=urlparse.urljoin(response.url, '?page=%s' % next_page)
            # self.log(url)
            yield Request(url, callback=self.parse)


    def parse_blog(self, response):
        hxs1=HtmlXPathSelector(response)
        summary="".join(hxs1.select("//div[@class='post']/div[@class='entry']/text()").extract())
        title=hxs1.select("//div[@class='post']/h2/a/text()").extract()[0]
        categories="".join(hxs1.select("//div[@class='post']/ul/li[@class='icon_cat']/a/text()").extract())
        tags=" ".join(hxs1.select("//div[@class='post']/ul/li[@class='icon_bullet']/a/text()").extract())
        cmt=hxs1.select("//div[@class='entry']").extract()[0]
        result=re.sub(r'<[^>]*?>','',cmt)
        item=LaozhaocrawlItem(title=title,summary=summary,categories=categories,link=response.url,tags=tags,content=result)
        yield item
        # fp.write(title+'\r\n'+categories+'\r'+tags+'\r\n'+result)


class chenhaoSpider(BaseSpider):
    name="chenhao"
    start_urls=['http://coolshell.cn/']

    def parse(self, response):
        hxs=HtmlXPathSelector(response)
        page=hxs.select("//div[@class='wp-pagenavi']/span[@class='current']/text()").extract()[0]
        next_page=int(page)+1
        for per in hxs.select("//div[@class='post']"):
            bloglink=per.select("h2/a/@href").extract()[0]
            # fp.write("******"+bloglink)
            yield Request(bloglink,callback=self.blog_parse)
        if next_page<=61:
            link="http://coolshell.cn/page/%s" % next_page
            yield Request(link,callback=self.parse)

    def blog_parse(self,response):
        hxs=HtmlXPathSelector(response)
        title=hxs.select("//div[@id='main']/div/h2/text()").extract()[0]
        content=hxs.select("//div[@class='post']/div[@class='content']").extract()[0]
        result=re.sub(r'<[^>]*?>','',content)
        categories=" ".join(hxs.select("//div[@class='under']/span[2]/a/text()").extract())
        tags=" ".join(hxs.select("//div[@class='under']/span[4]/a/text()").extract())
        fp.write(title+'\r\n'+categories+'\r'+tags+'\r\n'+result)
        # yield LaozhaocrawlItem(title=title,content=result,tags=tags,categories=categories,link=response.url,summary=None)
