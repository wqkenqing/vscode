#!python3
# coding=utf-8

with  open("/Users/wqkenqing/Desktop/out/reptile/fumian2.txt","r", encoding="utf8") as f:

        with open("/Users/wqkenqing/Desktop/out/reptile/done3.txt","w",encoding="utf8") as w:
            res=f.readline()
            while(res!=""):
                w.write("\"{}\",".format(res.replace("\n","")))
                w.write("\n")
                res = f.readline()
        w.close()
        f.close()



