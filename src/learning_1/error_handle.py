# file_name = input('please input the file name')
# fo = open(file_name)
# for eachline in fo:
#     print(eachline)

list = ['Varasekie', 1, [1, 2, 3]]
list1 = []
assert len(list)


#
# try:
#
#     with open('a file.txt','wb') as f
#
#         f.writelines('hello world')
#         sum = '1'+ 1
#         ####此处可以去除关闭文件这一步骤，因为py会自动检测这个文件
#
# except AssertionError as reason:
#     print('problem is' + str(reason))
# except TypeError as reason :
#     print('类型错误')
# except:
#     print('wrong')
####最后finally也可以被删掉

#raise TypeError

# class girl():
#     ####定义传进来的参数
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     ####注意这里的函数名不能和变量名重复，否则会导致py报错
#     def itage(self):
#         print('my age is ' + str(self.age))
#
#     def itgrade(self):
#         print('her grades is ' + str (self.grade))
#
# varasekie = girl('vara',13,6)

class Dog():
    # 方法__init()__是一个特殊的方法
    # 给予了self,name,age三个形参，并且self形参必不可少，并且放在第一个
    # 每当你根据Dog类创建新实例时，Python都会自动运行它
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 每一个与类相关联的方法调用都自动传递实参self
    # 它是一个指向实例本身的引用，让实力能够访问类中的属性和方法
    # 以self为前缀的变量都可供类中所有方法使用，我们还可以通过类的任何实例来访问这些变量
    def sit(self):
        print(self.name.title() + "sit!")

    def roll_over(self):
        print(self.name.title() + "roll over!")

    def __hide(self):
        print("the hidden thing")

samoyed = Dog('samoyed',13)

# samoyed.__hide()
samoyed._Dog__hide()
