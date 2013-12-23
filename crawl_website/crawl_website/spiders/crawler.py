from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from scrapy.utils.response import get_base_url
from urlparse import urljoin
import os

class CrawlerItem(Item):
    reference_link = Field()
    links = Field()

class CrawlerSpider(CrawlSpider):

    name = 'crawler'
    allowed_domains = []
    start_urls = []
 
    def __init__(self):
        for line in open('domain.txt', 'r'):
            columns = line.split(' ')
            if len(columns) >= 2:
                a = columns[0]
                b = columns[1]
            self.allowed_domains.append(a)
            self.start_urls.append('http://' + a)
            global filename
            a = a.replace(".","_")
            a = a + b.replace("\n","")
            filename = a + ".csv"
            self.url_type = b.replace("\n","")
        super(CrawlerSpider,self).__init__()
   
    rules = [Rule(SgmlLinkExtractor(allow=()), follow=True, callback='parse_item')]     


    def parse_item(self, response):
        sel = HtmlXPathSelector(response)
        links = sel.select('//a[contains(@href, "{0}")]/@href | /html/head/link[@type="application/{0}+xml"]/@href'.format(self.url_type)).extract()
        items = []
        for link in links:
            item = CrawlerItem()
            item['reference_link'] = response.url
            base_url = get_base_url(response)
            item['links'] = urljoin(base_url,link)
            items.append(item)
        if not os.path.exists("results"):
            os.makedirs("results")
        fields = ["reference_link", "links"] 
        with open(os.path.join("results",filename),'a+') as f:
            for item in items:
                f.write("{0}\n".format(','.join(str(item[field]) for field in fields)))