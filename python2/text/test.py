#!python3
# -*- coding:utf8 -*-
import logging
class TextOperate(object):
    logging.basicConfig(level=logging.INFO)
    def readFile(self,path,name):
        with open(path,encoding='utf8') as f:
            logging.info('ok')
            print(f.readlines())

    def getFileCount(self, path, name):
        with open(path,encoding='utf8') as f:
            logging.info('ok')
            list=f.readlines()
        return len(list)



if __name__ == '__main__':
    path="/Users/wqkenqing/Desktop/key_value.txt"
    ## 获取文件行数

    opearte= TextOperate()
    res=opearte.getFileCount(path,name="")
    print("file's count is {}".format(res))
