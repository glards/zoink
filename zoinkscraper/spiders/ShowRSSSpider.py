from scrapy.selector import XmlXPathSelector
from zoinkscraper.items import ZoinkscraperItem
from scrapy.spider import BaseSpider
from datetime import datetime

class ShowRSSSpider(BaseSpider):
	domain_name = "karmorra.info"
	start_urls = [ "http://showrss.karmorra.info/feeds/all.rss" ]

	def parse(self, response):
		xxs = XmlXPathSelector(response)
		xxs.register_namespace("f", "http://www.w3.org/2005/Atom")
		entries = xxs.select('//item')
		for entry in entries:
			item = ZoinkscraperItem()

			item['name'] = entry.select('./title/text()')[0].extract_unquoted()
			item['url'] = entry.select('./link/text()')[0].extract()

			item['date'] = datetime.strptime(entry.select('./pubDate/text()')[0].extract()[:-6],'%a, %d %b %Y %H:%M:%S')
			yield item

SPIDER = ShowRSSSpider()
