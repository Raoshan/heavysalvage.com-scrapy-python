from email.mime import image
import scrapy
import pandas as pd
df = pd.read_csv('F:\Web Scraping\keywords.csv')
base_url = 'https://www.heavysalvage.com/listings/index?search={}&within=&zip='

class SalvageSpider(scrapy.Spider):
    name = 'salvage'
    def start_requests(self):
        for index in df:
            yield scrapy.Request(base_url.format(index), cb_kwargs={'index':index})

    def parse(self, response, index):
        products = response.css(".card--listing")
        print(len(products))
        for product in products:
            print("***********************")
            name = product.css('.card-title a::text').get()
            print(name)
            item_type = index
            print(item_type)
            product_link = "https://www.heavysalvage.com"+product.css('.card-title a::attr(href)').get()
            print(product_link)
            image_link = product.css('.img-fluid::attr(src)').get()
            print(image_link)
            lot_id = product.xpath("//div[@class='card-block']/div[1]/text()").get().strip()
            print(lot_id)
            end_date = product.xpath("//div[@class='card-block']/div[2]/text()").get().strip()
            print(end_date)
            location = product.xpath("//div[@class='card-block']/div[3]/text()").get().strip()
            print(location)
            auction_Type = "yes"
            auctioneer = ""
            site_name = "heavysalvage"
            description =""

   