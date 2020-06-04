#!python3
# -*- coding: UTF-8 -*-
class Student(object):
    name
    ## 构造方法
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sayHello(self):
        print("hello")


ken=Student("ken",20)
ken.score=90

print(ken.name)
print(ken.age)
print(ken.score)

ken.sayHello()