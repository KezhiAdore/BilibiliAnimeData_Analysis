# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeDataItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    play=scrapy.Field()
    fllow=scrapy.Field()
    barrage=scrapy.Field()
    tags=scrapy.Field()
    pass
