# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()  # 排名序号
    title = scrapy.Field()  # 电影名称
    link = scrapy.Field()  # 电影详情链接
    rating = scrapy.Field()  # 电影评分
    participants = scrapy.Field()  # 参评人数
    quote = scrapy.Field()  # 最新评论
