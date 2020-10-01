import base64


def photo_base64():
    photo_path = '1.png'
    f = open(photo_path, 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()


def base64_photo():
    # bs:64编码
    bs = 'iVBORw0KGgoAAAANSUhEUg....'
    img_data = base64.b64decode(bs)
    file = open('2.jpg', 'wb')
    file.write(img_data)
    file.close()
