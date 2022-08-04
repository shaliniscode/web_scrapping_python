from pydoc import describe
import re
import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess



class FeaturesTestSpider(scrapy.Spider):
    name = 'features_test'
    allowed_domains = ['www.octoparse.com']
    start_urls = ['http://www.octoparse.com/']
    
    process = CrawlerProcess(settings={
    "FEEDS": {
        "items.csv": {"format": "csv"},
    },
        })

    #custom_settings: {"FEEDS": {"features.csv": {"format": "csv" }}}
    
    def parse(self, response):
        print("processing:"+response.url)
        #Extract data
        heading =[]
        description =[]
    
        #title = response.xpath("//section[@class='flex flex-column']/h2/a/text()").getall()
        heading.append(response.xpath("//div[@class='block flex-one']/h3/text()").extract())
        description.append(response.xpath("//div[@class='block flex-one']/p/text()").extract())
        
        scrapped_info = pd.DataFrame({'features':heading, 'Description':description})
             
        yield scrapped_info


if __name__ == "__main__":

    process = CrawlerProcess()
    process.crawl(FeaturesTestSpider)
    process.start()