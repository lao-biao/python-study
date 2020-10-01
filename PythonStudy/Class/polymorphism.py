"""
多态

形参为父类对象，调用不同子类执行不同效果
"""


class Person:

    def __init__(self, name):
        self.name = name

    def work(self):
        print("working")


class Coder(Person):

    def work(self):
        print("coding")


class Designer(Person):

    def work(self):
        print("designing")


class Project:

    # @staticmethod
    def toWork(self, person):
        person.work()


project = Project()
coder = Coder("Coder")
designer = Designer("Designer")
project.toWork(coder)  # coding

project.toWork(designer)  # designing

list_test = [1, 2, 3, 4]
list_test.pop()
tuple_test = (1, 2, 3, 4)
list_test.extend(tuple_test)
print(list_test)

dic = {"a": "1"}
del dic["a"]
print(dic)
