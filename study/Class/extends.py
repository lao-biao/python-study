"""
单继承
"""


class Person:
    __sex = None

    def eat(self):
        print("eating")

    def sleep(self):
        print("sleepping")


class Man(Person):
    __sex = "man"


class Women(Person):
    __sex = "female"


class Coder(Person):

    def code(self):
        print("coding")


class Boss(Man, Coder):

    def __init__(self):
        print("Manager")

    # override重写
    def code(self):
        # super().code()
        Coder.code(self)
        print("check")


coder = Coder()
coder.eat()
coder.sleep()
coder.code()

boss = Boss()
boss.sleep()
boss.code()
