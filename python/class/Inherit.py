#!python3
# -*- coding: UTF-8 -*-
class Teacher():
    def teach(self):
        print("teaching")

class MathTeacher(Teacher):
    def teach(self):
        print("math is teaching")

class EnlishTeacher(Teacher):
    def teach(self):
        print("english is teaching")
     
class ChineseTeacher(Teacher):
    def teach(self):
        print("chinese is teaching")

def showTeach(teach):
    teach.teach()



class IT(object):
    def teach(self):
        print("it is teaching")

it=IT()

mteacer=MathTeacher()

print(isinstance(mteacer,Teacher))




    
    