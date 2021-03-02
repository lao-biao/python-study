"""
测试元组和字典的拆包
"""


def func(*args, **kwargs):
    print(args)
    print(kwargs)


gl_nums = {1, 2, 3, 4}
gl_dict = {"name": "ZhangSan", "age": 20}

# 元素均被传递为元组
func(gl_nums, gl_dict)
# 拆包语法
func(*gl_nums, **gl_dict)
# 一般形式
func(1, 2, 3, 4, name="ZhangSan", age=20)

table = dir(func())
for item in table:
    print(item)

print(dir(func()))


if __name__ == "__main__":
    print("current is main thread")
