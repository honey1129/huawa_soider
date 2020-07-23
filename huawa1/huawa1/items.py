# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Huawa1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    store_id = scrapy.Field()
    store_grade= scrapy.Field()
    store_name= scrapy.Field()
    member_id= scrapy.Field()
    member_name= scrapy.Field()
    order_count= scrapy.Field()
    score= scrapy.Field()
    phone= scrapy.Field()
    store_qq= scrapy.Field()
    store_email= scrapy.Field()
    store_address= scrapy.Field()
    page= scrapy.Field()
    area_info = scrapy.Field()
