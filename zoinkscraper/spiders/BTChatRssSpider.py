from scrapy.selector import XmlXPathSelector
from zoinkscraper.items import ZoinkscraperItem
from scrapy.spider import BaseSpider
from datetime import datetime

class BTChatRssSpider(BaseSpider):
	domain_name = "bt-chat.com"
	start_urls = [
		"http://rss.bt-chat.com/?group=3&cat=9",
		"http://rss.bt-chat.com/?group=2&cat=9",
	]

	def parse(self, response):
		xxs = XmlXPathSelector(response)
		entries = xxs.select('//item')
		for entry in entries:
			item = ZoinkscraperItem()
			
                        item['name'] = entry.select('./title/text()')[0].extract_unquoted()
                        item['url'] = entry.select('./link/text()')[0].extract()

                        item['date'] = datetime.strptime(entry.select('./pubDate/text()')[0].extract()[:-4],'%a, %d %b %Y %H:%M:%S')
                        yield item
SPIDER = BTChatRssSpider()
