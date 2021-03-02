# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanmoviePipeline:
    def process_item(self, item, spider):
        print('排名TOP：'+item['rank'][0])
        print('电影名称：'+item['title'][0])
        print('详情链接：'+item['link'][0])
        print('豆瓣评分：'+item['rating'][0]+'('+item['participants'][0]+')')
        print('最新评论：'+item['quote'][0])
        return item
