"""
异常捕获
"""


# ZeroDivisionError: division by zero
# print(2 / 0)

def func():
    dd = 1
    if dd < 2:
        raise Exception("dd小于2")


func()

try:
    num = int(input("请输入整数"))
    res = 10 / num
    print(res)
except Exception as result:
    print("未知错误%s" % result)
finally:
    print("*" * 50)
