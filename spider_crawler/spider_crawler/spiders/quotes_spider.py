import scrapy
import re
from ..items import SpiderCrawlerItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from bs4.element import Comment
class QuotesSpider(CrawlSpider):
    name = "uic_crawler"
    start_urls = [
        'https://cs.uic.edu/'
    ]
    count = 0
    visited_links=set()
    allowed_domains=['uic.edu']
    # custom_settings ={
    #     'DEPTH_LIMIT':20
    # }
    #le=LinkExtractor()
    #rules = [Rule(LinkExtractor(allow = 'uic.edu'), callback='parse_data', follow=True)]

    rules = [Rule(LinkExtractor(deny=('#','\?','tel:','mailto:','login'),allow_domains=('uic.edu'),deny_domains=('login.uic.edu','.com','.net',"doc","?",'google.com'),
                                deny_extensions=('pdf','zip','img'),unique=True,canonicalize=True), callback='parse_data', follow=True)]
    
    def tag_visible(self,element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]','footer','menu','img','form','input','noscript','svg','path']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def parse_data(self, response):
    
        origin_url = response.url.replace('http:','https:')
        if origin_url not in self.visited_links:
            self.visited_links.add(origin_url)

            items=SpiderCrawlerItem()
            items['url']=origin_url
            items['title']=response.css('head title::text').extract_first().strip()
            soup = BeautifulSoup(response.text,"lxml")
            for div in soup.find_all("div", {'class': 'browser-stripe'}):
                div.decompose()

            contents = soup.findAll(text=True)
            visible_texts = filter(self.tag_visible, contents) 
            items['content']=" ".join(t.strip() for t in visible_texts)
            
            
            # str1 = response.xpath('//p/text()').getall()
            # items['content'] = ''.join(str1)
            print("Crawling:"+response.url)
            self.count+=1
            print(self.count)
            #print(items['content'])
            links = LinkExtractor(allow=('uic.edu'),deny=('.com'),canonicalize=True,unique=True).extract_links(response)
            links_unique=set()
            for link in links:
                if link.url != response.url:
                    links_unique.add(link.url.replace('http:','https:'))
            
            #links = response.xpath("//a/@href").extract()
            items['out_links']=links_unique


            # with open("sample.json", "w") as outfile: 
            #     outfile.write(json_object)

            yield items
        else:
            yield
        


        
