# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PortsaleItem(scrapy.Item):

    Property_Name = scrapy.Field()
    website = scrapy.Field()

    Dine_in = scrapy.Field()
    Takeout = scrapy.Field()
    Delivery = scrapy.Field()

    Address = scrapy.Field()
    Hours = scrapy.Field()
    Instrument = scrapy.Field()
    Sale_Price = scrapy.Field()
    pass
