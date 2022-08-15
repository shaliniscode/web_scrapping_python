from pydoc import describe
import re
import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess


scrapped_info = {}
desc=[]
class FeaturesTestSpider(scrapy.Spider):
    name = 'features_test'
    allowed_domains = ['www.octoparse.com']
    start_urls = ['http://www.octoparse.com/']
    
   
    #custom_settings: {"FEEDS": {"features.csv": {"format": "csv" }}}
    
    def parse(self, response):
        
        #Extract data
        heading = response.xpath("//div[@class='block flex-one']/h3/text()").extract()
        description = response.xpath('//div[@class="block flex-one"]/p').extract()

        for item in description:
           desc.append(( item.strip('<p>,</p>')).replace('<br>'," "))
     
        scrapped_info = dict(zip(heading, desc))
        print(scrapped_info)

    
        yield scrapped_info
        


if __name__ == "__main__":

    process = CrawlerProcess(settings={
    "FEEDS": {
        "features.csv": {"format": "csv"},
    }})
    process.crawl(FeaturesTestSpider)
    process.start()