#!python3
# -*- coding: UTF-8 -*-
class Teacher(object):


    def __init__(self,name,age,lession,add):
        self.__name=name
        self.__age=age
        self.__lession=lession
        self._add=add

    def introduce(self):
        print('my name is %s ' % self.__name)
        print('my  age is %d' % self.__age)
        print('my  lession is %s' % self.__lession)

    def getAge(self):
        return self.__age
    
    def setAgeLevel(self,age):
        if(age>20 and age <60):
            print("working")
        elif(age<20):
            print("intership")
        elif(age>=60):
            print("retire")
        

teacher=Teacher("joe",23,"math","LOS")        

print(teacher._add)
