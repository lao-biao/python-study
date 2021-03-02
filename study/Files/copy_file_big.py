# 编码格式
origin = open("../README.txt", encoding="UTF-8")
new = open("../README_NEW.txt", "wb")

# text = origin.read().encode("UTF-8")
# new.write(text)

# 读-写
while True:
    text = origin.readline().encode()
    # 判断是否读取到内容
    if not text:
        break
    new.write(text)

origin.close()
new.close()
