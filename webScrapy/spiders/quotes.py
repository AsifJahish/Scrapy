import scrapy

from ..items import WebscrapyItem

class QuoetesScrapes(scrapy.Spider):
    name = 'quotes'
    start_urls =[
        'https://quotes.toscrape.com/'
    ]


    def parse(self,response):
        # all_div_quotes= response.css('div.quote')
        # title= all_div_quotes.css('span.text::text').extract()
        # author= all_div_quotes.css('.author::text').extract()
        # tag= all_div_quotes.css('.tag::text').extract()
        #
        # yield {
        #     'title':title,
        #     'author':author,
        #     'tag':tag
        # }
        items= WebscrapyItem()

        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author= quotes.css('.author::text').extract()
            tag= quotes.css('.tag::text').extract()

            items['title']= title
            items['author']= author
            items['tag']=tag

            yield items