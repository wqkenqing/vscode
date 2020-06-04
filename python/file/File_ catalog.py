#!python3
# -*- coding: UTF-8 -*-
import os

# print(os.uname())
# print(os.environ)

# 路径操作

basepath=os.path.abspath(".")
newdir=os.path.join(basepath,'newdir')
# os.mkdir(newdir)
if(os.path.exists(newdir)):
    print('%s is created ' % (newdir))

os.rmdir(newdir)

if(os.path.exists(newdir)):
    print('%s is deleted ' % (newdir))
else:
    print('%s is deleted ' % (newdir))
