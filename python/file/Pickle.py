#--*-- encoding:utf8 --*--
import pickle
# import os
d=dict(name='ken',age=12,sex='boy')

##创建 file 操作对象

f=open("/Users/wqkenqing/Desktop/deploy_code/vscode/newdir/dump.txt","wb")


pickle.dump(d,f)
# data=pickle.loads(f)

# print(data)



