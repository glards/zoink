from zoinkscraper.items import ZoinkscraperItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from datetime import datetime

import re
import urlparse

torrentre = re.compile("<tr group=\"2\"><td><a href=\"(?P<Url>.*?)\">(?P<Name>.*?)</a></td><td class=\"modified\" val=\"(?P<Date>.*?)\">.*?</td><td class=\"size\" val=\".*?\">.*?</td><td class=\"type\">.*?</td></tr>", re.IGNORECASE | re.DOTALL)

class ZoinkSpider(BaseSpider):
    domain_name = "torrent.zoink.it"
    start_urls = [ "http://torrent.zoink.it/" ]

    def parse(self, response):
        self.log('Starting parse')
        for m in torrentre.finditer(response.body):
            self.log('Constructing item')
            item = ZoinkscraperItem()
            item['url'] = urlparse.urljoin(response.url, m.group('Url'))
            item['name'] = m.group('Name')
            item['date'] = datetime.fromtimestamp(long(m.group('Date')))
            yield item

SPIDER = ZoinkSpider()