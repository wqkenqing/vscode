# --*-- encoding:utf8 --*--

## 值传递 ,索引传递

## 值传递

a=1
b=['2',3]
c='sss'
def change(num):
    num=2

def change2(num):
    num.append("ok")
def change3(num):
    num+"22"

change(a)
change2(b)
change3(c)

print(a)
print(b)
print(c)


