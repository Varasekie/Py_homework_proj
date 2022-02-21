import numpy as np
import xlrd
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy import stats
import matplotlib.pyplot as plt

# 第一问数据读取，和一些简单初始化，如把催化剂拆分成一个数字表示的四元组（还没加）
data = xlrd.open_workbook(r"C:\Users\86139\Desktop\附件1.xlsx").sheets()[0]


def loaddata1(num):
    return [np.array([x.value for x in data.col(num - 1, col_dict[i], col_dict[i + 1])]) for i in range(0, 21)]


n = 0
col_dict = []
for i in data.col(0, 1):
    n = n + 1
    if i.ctype == 1:
        col_dict.append(n)
col_dict.append(n + 1)


def gettuple(n):
    key = data.cell(col_dict[n - 1], 0).value
    catalyst = data.cell(col_dict[n - 1], 1).value
    temperature = loaddata1(3)[n - 1]
    EthanolConversionRate = loaddata1(4)[n - 1]
    C4SelectionRate = loaddata1(6)[n - 1]
    return key, catalyst, temperature, EthanolConversionRate, C4SelectionRate


'''
实验类，包括实验的几个基本属性
初始化输入实验编号
fit函数用最小二乘法做拟合,参数1是次数，参数2为1（乙醇转化率）或2（C4选择性）
chazhi函数，n为1（乙醇转化率），2（c4选择性），m选择了几种插值方法
'''


class experiment:

    def __init__(self, n):
        data = gettuple(n)
        self.key = data[0]
        self.catalyst = data[1]
        self.temperature = data[2]
        self.ecRate = data[3]
        self.c4Rate = data[4]

    def chazhi(self, n, m):
        x = self.temperature
        xnew = np.linspace(x[0], x[-1], 500)
        if n == 1:
            y = self.ecRate
        elif n == 2:
            y = self.c4Rate
        if m == 1:
            print("test")
            f1 = interp1d(x, y)
            xlabel = "分段线性插值"
        elif m == 2:
            print("test")

            f1 = interp1d(x, y, 'quadratic')
            xlabel = "二次样条插值"
        elif m == 3:
            print("test")

            f1 = interp1d(x, y, 'cubic')
            xlabel = "三次样条插值"

        plt.rc('font', size=16)
        plt.rc('font', family='SimHei')
        y1 = f1(xnew)
        plt.plot(xnew, y1)
        plt.xlabel(xlabel)
        plt.show()
        return f1

    def chazhi(self):
        x = self.temperature
        xnew = np.linspace(x[0], x[-1], 500)
        y1 = self.ecRate
        y2 = self.c4Rate

        f1 = interp1d(x, y1, 'quadratic')
        f2 = interp1d(x, y2, 'quadratic')
        Y1 = f1(xnew)
        Y2 = f2(xnew)
        plt.rc('font', size=16)
        plt.rc('font', family='SimHei')

        plt.subplot(121), plt.plot(xnew, Y1)
        plt.xlabel("温度")
        plt.subplot(122)
        plt.plot(xnew, Y2)
        plt.xlabel("温度")
        # 相关性分析，n,1是乙醇，2是C4,m,1是皮尔逊，2是斯皮尔曼

    def xiangguan(self, n, m):
        if m == 1:
            if n == 1:
                # print("皮尔逊乙醇")
                r, p = stats.pearsonr(self.temperature, self.ecRate)
            if n == 2:
                # print("皮尔逊C4")
                r, p = stats.pearsonr(self.temperature, self.c4Rate)
        if m == 2:
            if n == 1:
                # print("斯皮尔曼乙醇")
                r, p = stats.spearmanr(self.temperature, self.ecRate)
            if n == 2:
                # print("斯皮尔曼C4")
                r, p = stats.spearmanr(self.temperature, self.c4Rate)
        return r, p


from scipy import stats

shiyan=[experiment(i) for i in range(1,22)]
# for i in shiyan:
#     print(i.key+"乙醇转化率插值图")
#     i.chazhi(1,2)
#     print(i.key+"C4选择率插值图")
#     i.chazhi(2,2)


for i in range(1, 22):
    b = experiment(i).chazhi()
    a = experiment(i)
    # r = a.xiangguan()
    # print(a.xiangguan())
    # if a.xiangguan(1, 1)[1] > 0.05:
    #     print(a.key)
    # if a.xiangguan(2, 1)[1] > 0.05:
    #     print(a.key)
    # if a.xiangguan(1, 2)[1] > 0.05:
    #     print(a.key)
    # if a.xiangguan(2, 2)[1] > 0.05:
    #     print(a.key)
    # print(a.xiangguan(1, 1), a.xiangguan(2, 1))
    print(a.xiangguan(1,2)[1])

