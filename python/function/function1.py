# --*-- encoding:utf8 --*--


## 关建字参数

def code(name,age,fond='no'):
    print(name)
    print(age)
    print(fond)


## 不定长参数

def code2(name,age,*fond):
    print(name)
    print(age)
    print(str(fond))

code2("中国","12",'羽毛球','篮球')


# code(age="12",name="kuiq")

