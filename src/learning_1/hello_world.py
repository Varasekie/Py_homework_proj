# str1 = 'HELLO'
# str2 = 'WORLD'
# str3 = 'HELLO'
# if str1 is str3:
#     print(str1 == str3)
# else:
#     print(str1 == str3)
#
# if str1 == str3:
#     print(str1 == str3)
# else:
#     print(str1 == str3)
#
# def test5(x,y=0,*a,**b):
#     print(x)
#     print(y)
#     print(a)
#     print(b)
#
# test5(18,3,4,5,6,name = 'Varasekie',sex = 'female')
#
# list1 = [123,456,123,789,123]
# #给列表的123计数
# print(list1.count(123))
# #reverse（）是反转列表，没有返回值
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# tuple = (1,2,3,4,5,6,7,8,9)
# # tuple = tuple[1:3]+tuple[4:7]
# # print(tuple)
#
# str1 = 'this is a string'
# str2 = str1.capitalize()
# print(str2)
# str3 = str1.title()
# print(str3)

# str4 = 'This is Another String'
# str5 = str4.casefold()
# print(str5)

# str = '123123'
# str1 = '2'
# print(str.replace('1',str1,1))
#
# str = 'Varasekie'
# print(str.split('a'))

# 位置参数
a = '{0} love {1} {2}'.format('Varasekie', 'writing', 'python')
print(a)

# 关键字参数
e = '{a} love {b} {c}'.format(a='Varasekie', b='writing', c='Java')
print(e)

# 位置参数和关键字参数混合使用，位置参数一定要在关键字参数之前
f = '{0} love {b} {c}'.format('Varasekie', b='writing', c='C')
print(f)

f = '{{0}}'.format('不打印')
print(f)

a = '{0:.1f} {1}'.format(127.75, 'GB')
print(a)

####函数
# def fun1(x):
#     def fun2(y):
#         return x*y
#     return fun2
#
#
# def fun3(x):
#     def fun4():
#         return 6
#     return fun4()
#
# print(fun3(2))
#
# def fun5():
#     def fun6():
#         return 3
#     return fun6()
#
# print(fun5())

# i = fun1(3)(2)
# print(i)
# i = fun1(4)(5)
# print(i)


#lambda表达式
# a = lambda x, y: x * y
# print(a(3, 4))
# b = filter(None, ['0', '1', 0, 1, True, False])
# print(list(b))
#
#
# def odd(x):
#     return x % 2
#
#
# temp = range(2, 10)
# a = filter(odd, temp)
# print(list(a))
#
# a = list(filter((lambda x: x % 2), range(3, 12)))
# print(a)
#
# a = list(map(lambda x: x + 3,range(0, 3)))
# print(a)

#字典
a =  dict(( (1,'Samoyed'),(2,'Varakie') ))
print(a)

a = dict(( [2,'varasekie'],[1,'samoyed'] ))
print(a)

dict1 ={}
dict1 = dict1.fromkeys((1,2,3),'value')
print(dict1)

dict2 = dict1.fromkeys((1,2,3),(4,5,6))
print(dict2)

dic3 = dict1.fromkeys(range(1,3),'ww')
print(dic3)

####遍历打印key（value同理）
for every in dic3.keys():
    print(every)




dict = dic3.get(4)
print(dict)
dict = dic3.get(1)
print(dict)

a = {1 :'one',2:'two'}
b = a.copy()
c = a
print(id(a))
print(id(b))
print(id(c))

# d = a.setdefault(1,'onee')
# print(d)
# e = a.setdefault(3,'three')
# print(e)
print(a)
a.update({'3':'three'})
print(a)

f = open('test.txt', 'w')
f.write('Varasekie')
f.close()

fo = open('test.txt', 'r')
data = fo.read()
print(data)


