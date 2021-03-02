"""
类方法和静态方法
"""


class Tool(object):
    # 类属性，记录工具的数量
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("Tool count==>%d" % cls.count)

    def __init__(self, name):
        self.name = name
        # 类属性的值+1
        Tool.count += 1

    @staticmethod
    def work():
        print("Tool is working")


knife = Tool("knife")
fork = Tool("fork")

Tool.show_tool_count()  # Tool count==>2
Tool.work()  # Tool is working
