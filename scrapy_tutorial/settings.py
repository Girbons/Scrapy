# Scrapy settings for scrapy_tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapy_tutorial'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrapy_tutorial.spiders']
NEWSPIDER_MODULE = 'scrapy_tutorial.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

