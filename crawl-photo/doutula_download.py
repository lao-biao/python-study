import requests
import re
from bs4 import BeautifulSoup


# 将doutula网站的图片储存在本地文件夹
# 有的图片地址有问题获取不到
# 注意：标题名中含有/时储存时会报错


# 以二进制的方式写入图片到本地images文件夹中
def crawl_image(image_url, image_local_path):
    r = requests.get(image_url, stream=True)
    try:
        with open(image_local_path, "wb") as f:
            f.write(r.content)
    except UnicodeDecodeError:  # 抛出异常
        print("save error")


# 筛选网页源码获取图片的url和title
def get_images_list(page=1):
    url = 'http://www.doutula.com/photo/list/?page={}'.format(page)
    # 伪装浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    # 获取p标签下的内容
    content = soup.find_all("img", class_="img-responsive lazy image_dta")
    # print(content)
    # html = requests.get('https://www.baidu.com').text
    # 正则表达式(.*？)表示所有内容
    reg = 'data-original="(.*?)".*?alt="(.*?)"'
    # 提高匹配效率
    reg = re.compile(reg, re.S)  # S:多行匹配
    images_list = re.findall(reg, str(content))
    for image in images_list:
        image_url = image[0]
        image_title = image[1]
        image_title = str(image_title).replace('/', '%')
        # format字符串格式化
        print("正在保存%s" % image_title)
        print(image_url)
        # 图片类型--格式
        photo_type = str(image_url.strip().split('/')[-1])
        photo_type = str(photo_type)[-4:]
        # print(photo_type)
        crawl_image(image_url, "./photos/" + image_title + photo_type)
    print('第' + str(page) + '页已保存')


# 获取1-10页的图片资源
if __name__ == '__main__':
    for i in range(1, 10):
        get_images_list(i)
