# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImagesdemoPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name = request.meta['name'] + '.jpg'
        return file_name

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['imgPath'], meta={'name': item['wareName']})

    # def process_item(self, item, spider):
    #     return item
