# Scrapy settings for laozhaoCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'laozhaoCrawl'

SPIDER_MODULES = ['laozhaoCrawl.spiders']
NEWSPIDER_MODULE = 'laozhaoCrawl.spiders'

ITEM_PIPELINES=[
    'laozhaoCrawl.pipelines.LaozhaocrawlPipeline',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'laozhaoCrawl (+http://www.yourdomain.com)'
