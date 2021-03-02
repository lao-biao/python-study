# 编码格式
origin = open("../README.txt", encoding="UTF-8")
new = open("../README_NEW.txt", "wb")

text = origin.read().encode("UTF-8")
new.write(text)

origin.close()
new.close()
