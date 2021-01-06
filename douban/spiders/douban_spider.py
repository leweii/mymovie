# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/people/lahmHe/collect']

    def parse(self, response):
    	movie_list = response.xpath("//div[@class='grid-view']//div//div[@class='info']//ul")
    	for m_item in movie_list: 
    		movie_item = DoubanItem()
    		movie_item['movie_name'] = m_item.xpath(".//li[@class='title']//a//em[1]//text()").extract_first()
    		yield movie_item

    	next_link = response.xpath("//div[@class='paginator']//span[@class='next']//link//@href").extract()
    	if next_link:
    		next_link = next_link[0]
    		yield scrapy.Request("https://movie.douban.com" + next_link, callback=self.parse)
    		