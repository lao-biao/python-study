"""
私有属性和私有方法
"""


class Women:
    # 私有属性
    __age = 20

    def __init__(self, name):
        self.name = name
        pass

    def secret(self):
        print("%s的年龄是%d" % (self.name, self.__age))

    def __sing(self):
        pass


girl = Women("Mary")
# 私有属性在外界不能直接访问
# print(girl.__age)

girl.secret()
# 私有属性在外界不能直接访问
# girl.__sing()
