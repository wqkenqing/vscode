#--*- encoding:utf8 --*--

def sayHello():
    res=input("key in please!\n")
    if(res=="ok"):
        print("login")
    else:
        print("login failed!")

# sayHello()

## 参数

### 默认参数

def defaultFunction(name="joe"):
    print(name)

defaultFunction("ken")


def keyFunction(name,age):
    print(name)
    print(age)

