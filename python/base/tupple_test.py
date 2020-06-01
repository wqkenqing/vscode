# --*-- encoding:utf8 --*--

tupple1=(1,"2","three")

tupple2=()

## 获取元组中的值

print(tupple1[1])

print(tupple1[:])

## 元组不可变,但元组中的元素若具备可变性,则对应位置该元素还是变化的可能

tupple3=("1",2,[3,4,5])
print(tupple3[2])

tupple3[2].append(6)
print(tupple3)
## 






