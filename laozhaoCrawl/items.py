# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class LaozhaocrawlItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title=Field()
    summary=Field()
    link=Field()
    categories=Field()
    tags=Field()
    content=Field()
