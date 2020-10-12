import scrapy
import json
from anime_data.items import AnimeDataItem

class AnimeSpider(scrapy.Spider):
    name = 'anime'
    #allowed_domains = ['https://www.bilibili.com']
    #番剧信息表api
    url_head="https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&season_type=1&pagesize=20&type=1"
    start_urls = [url_head+"&page=1"]

## 递归解析番剧信息表
    def parse(self, response):
        data=json.loads(response.text)
        next_index=int(response.url[response.url.rfind("=")+1:])+1
        if data['data']['size']==20:
            next_url=self.url_head+"&page="+str(next_index)
            yield scrapy.Request(next_url,callback=self.parse)
        for i in data['data']['list']:
            media_id=i['media_id']
            detail_url=("https://www.bilibili.com/bangumi/media/md"+str(media_id))
            yield scrapy.Request(detail_url,callback=self.parse_detail)
        pass

## 解析番剧详情页面
    def parse_detail(self,response):
        item=AnimeDataItem()
        #番剧名称
        item['name']=response.xpath('//span[@class="media-info-title-t"]/text()').extract()[0]
        #播放量
        item['play']=response.xpath('//span[@class="media-info-count-item media-info-count-item-play"]/em/text()').extract()[0]
        #追番数
        item['fllow']=response.xpath('//span[@class="media-info-count-item media-info-count-item-fans"]/em/text()').extract()[0]
        #弹幕数
        item['barrage']=response.xpath('//span[@class="media-info-count-item media-info-count-item-review"]/em/text()').extract()[0]
        #番剧标签
        item['tags']=response.xpath('//span[@class="media-tag"]/text()').extract()
        return item