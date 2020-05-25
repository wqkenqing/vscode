# -*- coding:utf8 -*-


list1=["1",2,"three"]
print(list1[0:2])

print("最大值是:")
print(max(list1))


## 最小值
print("最小值是:")
print(min(list1))

## 修改
print(list1)
list1[0]=1
print(list1)

## 添加

list1.append("four")
print(list1)

## 删除
del list1[2]

print(list1)

## 清空

print(list1)
del list1[:]
print(list1)

