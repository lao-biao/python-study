from scrapy import Request
import scrapy
from doubanMovie.items import DoubanmovieItem


class MoviespriderSpider(scrapy.Spider):
    name = 'moviesprider'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Referer': 'https://movie.douban.com/top250'
    }

    allowed_domains = ['douban.com']

    # start_urls = ['http://movie.douban.com/top250']

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        currentpage_movie_items = response.xpath('//div[@class="item"]')
        for movie_item in currentpage_movie_items:
            movie = DoubanmovieItem()
            movie['rank'] = movie_item.xpath('div[@class="pic"]/em/text()').extract()
            movie['title'] = movie_item.xpath(
                'div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            movie['link'] = movie_item.xpath('div[@class="pic"]/a/@href').extract()
            movie['rating'] = movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            movie['participants'] = movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[last()]/text()').extract()
            movie['quote'] = movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            yield movie
