class Changed(int):
    def __add__(self, other):
        ####继承了int类里面的sub方法，因此不会无限递归
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


a = Changed(3)
b = Changed(4)
print(a - b)

a = [1, 2, 3, 4]
c = {'key1': 'value1'}
d = 'Varasekie'
b = iter(a)
print(next(b))
print(next(b))

b = iter(c)
print(next(b))

b = iter(d)
print(next(b))

####利用迭代器，打印字符串
while True:
    try:
        each = next(b)
    except StopIteration:
        break
    print(each)


class Fib():
    def __init__(self):
        ####定义这两个是为了让下面其他的函数也能访问这个值
        self.a = 0
        self.b = 1

    def __iter__(self):
        ####返回迭代器（自身就是迭代器了
        return self

    def __next__(self):
        ####运用加减法
        # self.b = self.a + self.b
        # self.a = self.b - self.a
        ####或者利用同时赋值的方法
        self.a, self.b = self.b, self.a + self.b
        return self.a


fib = Fib()
for num in fib:
    if num < 20:
        print(num)
    else:
        print('end')
        break

a = 1
b = 2
a, b = b, a + b
print(a)
print(b)


def borner():
    print('一个生成器')
    ####利用yield，在2的地方停止，下一次从4开始，利用next（）迭代方法
    yield 2
    yield 4


####先具象化成某个参数
a = borner()
print(next(a))
print('中间暂停')
print(next(a))

####法二
b = borner()
for i in b:
    print(i)


####说明i可以自动检测到是否迭代完成，

def Libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a

for i in Libs():
    if i < 10 :
        ####使在一行上打印，避免分行打印
        print(i, end = ' ')
    else:
        print('end')
        break

a = [i for i in range(10) if not i % 2 == 0]
print(a)

b = { i : i % 2 == 0 for i in range(12) if not (i % 5 == 0) and not i % 3 == 0}
print(b)