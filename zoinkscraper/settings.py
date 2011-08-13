# Scrapy settings for zoinkscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# Or you can copy and paste them from where they're defined in Scrapy:
# 
#     scrapy/conf/default_settings.py
#
import os

os.environ['FLAVOR'] = 'prod'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

BOT_NAME = 'zoinkscraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['zoinkscraper.spiders']
NEWSPIDER_MODULE = 'zoinkscraper.spiders'
DEFAULT_ITEM_CLASS = 'zoinkscraper.items.ZoinkscraperItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'zoinkscraper.pipelines.ZoinkscraperPipeline'
]

LOG_LEVEL='DEBUG'
