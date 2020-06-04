#!python3
# coding=utf-8
import logging
import json

class TextOperate(object):
    logging.basicConfig(level=logging.INFO)

    def readFile(self, path, name):
        with open(path, encoding="utf8") as f:
            logging.info('ok')
            print(f.readlines())

    def getFileCount(self, path, name):
        with open(path, encoding='utf8') as f:
            logging.info('ok')
            list = f.readlines()
        return len(list)

    def splitFile(self, path):
        with open(path, 'r', encoding='utf8')as f:
            line = f.readline()
            while (line != ''):
                print(line)
                if (line.__contains__('\t')):
                    lines = line.split("\t")
                    if (lines[len(lines) - 1].__contains__("{")):
                        last=json.loads(lines[len(lines)-1])
                        for kv in last.items():
                            print(kv)
                line = f.readline()


if __name__ == '__main__':
    path = "/Users/wqkenqing/Desktop/key_value.txt"
    ## 获取文件行数
    opearte = TextOperate()
    opearte.splitFile(path)
