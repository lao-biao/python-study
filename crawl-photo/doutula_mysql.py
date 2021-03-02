import requests
import re
import pymysql

# 将图片的网址和标题储存在本地数据库
# 连接本地数据库
db = pymysql.connect(host='127.0.0.1', port=3306, db='study', user='root', password='root', charset='utf8')
# 获取游标
cursor = db.cursor()


# 测试连接
def test():
    cursor.execute('select * from images')
    print(cursor.fetchall())


# 筛选网页源码获取图片的url和title
def get_images_list(page=1):
    url = 'https://www.doutula.com/photo/list/?page={}'.format(page)
    # print(url)
    # 伪装浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    html = requests.get(url=url, headers=headers).text
    # print(html)
    # html = requests.get('https://www.baidu.com').text
    # 正则表达式(.*？)表示所有内容
    reg = 'data-original="(.*?)".*?alt="(.*?)"'
    # 提高匹配效率
    reg = re.compile(reg, re.S)  # S:多行匹配
    images_list = re.findall(reg, html)
    for image in images_list:
        image_url = image[0]
        image_title = image[1]
        # format字符串格式化
        cursor.execute("insert into images(`url`,`title`) values ('{}','{}')".format(image_url, image_title))
        print("正在保存%s" % image_title)
        db.commit()


# 爬取
def crawl(start, end):
    # 获取start-end页的图片资源
    for i in range(start, end):
        get_images_list(i)


# 通过关键字查找
def search(keyword):
    cursor.execute('select * from images where title like "%{}%"'.format(keyword))
    # print(len(cursor.fetchall()))
    result_tuple = cursor.fetchall()
    for result in result_tuple:
        print(result)


if __name__ == "__main__":
    # test()
    # search('测试')
    # crawl(2, 10)
    search('傻')
