class Cat():

    def __init__(self,age,name):
        ####此处定义的，是每次在声明一个class的时候，都需要默认传入的参数
        ####此处定义了self.age =  age，之后就在调用age的时候，就不用
        self.age =  age
        self.name = name

    def itsname(self):
        print(self.name)

    def itsage(self):
        print(self.age)

    def itstype(self,type):
        ####当在调用某个函数才需要某个参数时，可以通过这样定义函数
        self.type = type
        print(self.type)

persian = Cat(5,'balloon')
persian.itsage()
persian.itsname()



s = Cat(6,'yuuki3')
s.type = 5
s.itstype('mois')

class A:
    pass
class B(A):
    pass

####判断B是否为A的字类
print(issubclass(B,A))

####判断某个对象是否在A内
b = B()
print(isinstance(b,A))
print(isinstance(b,B))
print(isinstance(B,A))

class C():
    def __init__(self,name):
        self.name = name

c = C('Kate')
print(hasattr(c,'name'))

d = C('Vara')
####找不到name时返回default
e = getattr(d,'age','not find the related information')
print(e)

####找不到的时候，创建一个name的key
setattr(d,'type','persian')
print(d.type)

# delattr(d,'type')
# # print(d.type)
# # ####此时会报错

class D():
    def __init__(self,number = 1):
        self.num = number

    def getnum(self):
        return self.num

    def changeNum(self,newNum):
        self.num = newNum


    def delNum(self):
        del self.num

    x = property(getnum,changeNum,delNum)

####当__init__传入的参数中有某一个的时候
d = D()

####如果直接调用，说明是打印值
print(d.x)
####1

####    =时相当于执行第二个函数，重新赋值
d.x = 3
print(d.num)
####3

####删除x（不要操作，会导致很多bug
# del d.x
# print(d.getnum)
####这一句是会报错的，
####由于删除了x之后，也不能调用其他的被包含在property函数中的函数

del A
del B
####魔方方法
class A():
    def __init__(self,name):
        self.name = name

    def changeName(self,newName):
        self.name = newName


####设置一个B类，来继承str类
class B(str):
    def __new__(cls, str):
        return str.upper()
    def __init__(self):
        super.__init__(str)





b = B('bird')
print(b)



class C():
    def __init__(self):
        print('__init__()')

    def __del__(self):
        print('__del__')

    def printC(self):
        print('CCC')


c = B('cat')
d = c
f = d
####这里的cdf都是对这个B（‘cat’）的引用
####当直接引用被删除的时候，才会调用__del__(self)
del d



x = C()
y = x
z = y
####只要删除直接引用，就会
del z

y.printC()



