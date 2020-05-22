# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeurlsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    date_of_publishing = scrapy.Field()
    link = scrapy.Field()
    date_of_scraping = scrapy.Field()
    text = scrapy.Field()
