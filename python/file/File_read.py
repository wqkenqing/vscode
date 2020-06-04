#!python3
# -*- coding: UTF-8 -*-
import logging
## file open 
# try:
#     f = open('/Users/wqkenqing/Desktop/key_value.txt', 'r')
#     for line in f.readlines():
#         print(line.strip()) # 把末尾的'\n'删掉

# finally:
#     if f:
#         f.close()
    
## file write 

with open("/Users/wqkenqing/Desktop/key2.txt","wb") as f:
    f.write("hello world ")
                