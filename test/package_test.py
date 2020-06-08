#!python3
# coding=utf-8
from package.test1 import test
from package2.test2 import test2

if __name__ == '__main__':
    t=test()
    t2=test2()
    t.ouput()
    t2.output()

