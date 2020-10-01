"""
文件操作的学习

open() 打开文件，并返回文件对象

read() 将文件内容读取到内存

write() 将指定内容写入文件

close() 关闭文件


"""
with open("../README.txt", "rb") as f:
    content = f.read()
    # 编码
    print(content.decode())
    # 关闭文件
    f.close()
