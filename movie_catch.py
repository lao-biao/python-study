import re
import json
import requests


# 抓取百度搜索页面'电影'的结果
# chrome抓包
def catch(page=1):
    pn = (page - 1) * 8  # 这个pn值是每页都在变化的，以8递增
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28286&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E7%94%B5%E5%BD%B1&sort_key=16&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=" + str(
        pn) + "&rn=8&cb=jQuery110204230762934017789_1575516372377&_=1575516372379"
    res = requests.get(url)
    json_str_re = re.compile("{.*}")
    json_str = json_str_re.search(res.text).group()
    movie_dict = json.loads(json_str)
    for movie in movie_dict["data"][0]["result"]:
        print(movie["ename"])


if __name__ == '__main__':
    for child in range(1, 10):
        catch(child)
