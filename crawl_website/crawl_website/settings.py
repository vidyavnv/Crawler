# Scrapy settings for crawl_website project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawl_website'

SPIDER_MODULES = ['crawl_website.spiders']
NEWSPIDER_MODULE = 'crawl_website.spiders'

SPIDER_MIDDLEWARES = {
	'crawl_website.custom_filters.SeenURLFilter' : 100
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawl_website (+http://www.yourdomain.com)'
