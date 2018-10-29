import scrapy
import request
import urllib
import json
import re

from image_crawler.items import ImageItem, Mp4Item


class imagur_crawler(scrapy.Spider):
    name = "imagur"

    def start_requests(self):
        url = "https://api.imgur.com/3/gallery/hot/time/"
        end = "?IMGURPLATFORM=web&IMGURUIDJAFO=632455f5bfab91890baf550dd27ee7c87457141a80094222e6cc210aba7d4993&SESSIONCOUNT=1&client_id=546c25a59c58ad7&realtime_results=false&showViral=true"
        # start_urls = [url+1+end]
        for i in range(20):
            yield scrapy.Request(url=url + str(i) + end, callback=self.parse)

    def parse(self, response):
        jsonResponse = json.loads(response.body_as_unicode())
        for data in jsonResponse['data']:
            item = Mp4Item()
            item['mp4name'] = data['images'][0]['id']
            item['mp4url'] = data['images'][0]['link'].replace("mp4", "gifv")
            # item['image_urls'] = [data['images'][0]['link'].replace("mp4", "gifv")]
            yield item
            # detailUrl = "https://imgur.com/gallery/" + data['link']
            # yield scrapy.Request(url=detailUrl, callback=self.parseDetail)
        # self.log('Saved file %s' % response.body)

    # def parseDetail(self, response):
    #     item = ImagurItem()
    #     item['image_urls'] = "https://imgur.com/gallery/" + content['id']
    #     yield item