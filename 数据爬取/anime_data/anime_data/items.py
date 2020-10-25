# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeDataItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()   #番剧名称
    play=scrapy.Field()     #总播放量
    follow=scrapy.Field()    #追番人数
    barrage=scrapy.Field()  #弹幕数量
    tags=scrapy.Field()     #番剧标签，列表形式
    pass
