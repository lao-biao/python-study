"""
dir内置函数
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

"""

"""
class Test:
    pass


a = Test()
a.name = "A"
print(a.name)
"""

"""
class Person:
    def __init__(self):
        self.name = "Tom"

    def __del__(self):
        print("deleted")


person = Person()
print(person.name)
del person
"""


class A:
    def __init__(self):
        print("初始化")

    def __del__(self):
        print("销毁前")

    # print()默认输出16进制的地址值
    def __str__(self):
        # 必须返回一个字符串
        return "A"


a = A()
print(a)
del a
