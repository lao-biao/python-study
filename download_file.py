import requests

"""
用于下载文件使用
"""

url = "https://ww2.mathworks.cn/content/dam/mathworks/ebook/gated/cn-deep-learning-vs-machine-learning-ebook.pdf"
file_name = "ebook.pdf"

with open(file_name, 'wb') as f:
    f.write(requests.get(url, stream=True).content)
