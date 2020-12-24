# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from imagesDemo.items import ImagesdemoItem


class ImagesspiderSpider(scrapy.Spider):
    name = 'imagesSpider'
    allowed_domains = ['ch.jd.com']
    start_urls = ['http://ch.jd.com/']

    def start_requests(self):
        url = 'http://ch.jd.com/hotsale2?cateid=686'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        products = data['products']
        for image in products:
            item = ImagesdemoItem()
            item['wareName'] = image.get('wareName').replace('/', '')
            item['imgPath'] = 'http://img12.360buyimg.com/n1/s320x320_' + image.get('imgPath')
            yield item



if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('imagesSpider')
    process.start()
