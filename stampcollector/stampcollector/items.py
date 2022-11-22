# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StampcollectorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    section=scrapy.Field()
    subsection_id=scrapy.Field()
    origin_E=scrapy.Field()
    origin_W=scrapy.Field()
    end_E=scrapy.Field()
    end_W=scrapy.Field()
    distance=scrapy.Field()
    time_E=scrapy.Field()
    time_W=scrapy.Field()
    elevation_E=scrapy.Field()
    elevation_W=scrapy.Field()