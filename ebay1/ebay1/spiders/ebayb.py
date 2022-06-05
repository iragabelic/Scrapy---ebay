import scrapy


class EbaybSpider(scrapy.Spider):
    name = 'ebayb'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=iphone+12+pro&_sacat=0']

    def parse(self, response):
         title = response.css(".s-item__title::text").extract()
         price = response.css(".s-item__price::text").extract()
         condition = response.css(".SECONDARY_INFO::text").extract()

         for item in zip(title, price, condition):
             scraped = {

                'title' : item[0],
                'price' : item[1],
                'condition' : item[2],
             }
             yield scraped




