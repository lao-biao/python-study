"""
私有属性和私有方法
"""


class Women:
    # 私有属性

    def __init__(self, name):
        self.name = name
        self.__age = 20

    def secret(self):
        print("%s的年龄是%d" % (self.name, self.__age))

    def __sing(self):
        print("%s在唱歌" % self.name)


girl = Women("Mary")
# 私有属性在外界不能直接访问
print(girl._Women__age)

girl.secret()
# 私有属性在外界不能直接访问
girl._Women__sing()
