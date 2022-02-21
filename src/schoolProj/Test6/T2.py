import math
class Equation:
    # 初始化，输入参数
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # 判断判别式
    def getData(self):
        return self.b * self.b - 4 * self.a * self.c

    # 获得第一个根
    # 如果判别式为负，返回0.
    def getRoot1(self):
        if self.getData() < 0:
            return 0
        else:
            return (-1 * self.b + math.pow(self.getData(), 1 / 2)) / 2 / self.a

    # 获得第二个根
    # 如果判别式为负，返回0.
    def getRoot2(self):
        if self.getData() < 0:
            return 0
        else:
            return (-1 * self.b - math.pow(self.getData(), 1 / 2)) / 2 / self.a

e1 = Equation(1, 4, 5)
e2 = Equation(1, 4, 3)
print("第一个方程的",'第一个根为',e1.getRoot1(),'第二个根为',e1.getRoot2())
print('第二个方程的','第一个根为',e2.getRoot1(),'第二个根为',e2.getRoot2())

