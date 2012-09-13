from scrapy.selector import HtmlXPathSelector, XmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.contrib.spiders import XMLFeedSpider
from elections2012.items import StoryItem
from xml.dom.minidom import parseString
from datetime import datetime
import rfc822

class spider1(XMLFeedSpider):
    name='elections2012'
    start_urls = ['http://online.wsj.com/xml/rss/3_7087.xml']

    itertag = 'item'

    def parse_node(self, response, node):
        item = StoryItem()

	title = node.select('title').extract()
        description = node.select('description').extract()
        link = node.select('link').extract()
	pubDate = node.select('pubDate').extract()	
	
		
	item['title'] = parseString(title[0].encode('utf-8')).firstChild.firstChild.toxml()
	item['description'] = parseString(description[0].encode('utf-8')).firstChild.firstChild.toxml()
	item['link'] = parseString(link[0].encode('utf-8')).firstChild.firstChild.toxml()
	item['source'] = 'bbc'
	item['pubDate'] = datetime.strptime(parseString(pubDate[0]).firstChild.firstChild.toxml()[:-4], '%a, %d %b %Y %H:%M:%S')
	item['created'] = datetime.now()

	return item 

