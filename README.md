Crawler
=======

Crawling set of domains.  

How to use:  
1. Install scrapy  
2. On Terminal, change directory to crawl_website and run this command: ./crawl_web.sh  


domain.txt contains a list of domains along with type of data required(rss,pdf, etc.)  

crawl_web.sh creates a spider 'crawler' which crawls through the domains specified in 'domain.txt' and creates 'results' folder in which csv file is generated for each domain.
