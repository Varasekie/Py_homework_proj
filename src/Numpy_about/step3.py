import numpy as np
import pandas as pd
from scipy.optimize import leastsq  # 这里就是我们要使用的最小二乘的函数
import pylab as pl


def rush(a, string):
    # 清洗数据
    # 去除NaN
    global avalue
    a = a.dropna()

    # 提取估值数据这一列的值，除去0
    a = a[~ a[string].isin([0])]

    a = a.dropna()

    # 两个特有的索引
    if string == '估值数据':
        # 洗掉市效率异常
        avalue = a[string]
        a = a.drop(avalue[avalue > 10].index)
        a = a.drop(avalue[avalue == 0].index)
        # 洗掉基本面异常


    else:
        if string == '估值指标':
            avalue = a[string]
            a = a.drop(avalue[avalue > 10].index)
            a = a.drop(avalue[avalue == 0].index)
            # print(a)
        else:
            print('wrong')
    # 其他几个共有的索引，清洗为0的数据
    a = a.drop(a['基本面数据'][a['基本面数据'] == 0].index)
    a = a.drop(a['Unnamed: 5'][a['Unnamed: 5'] == 0].index)
    # a = a.drop(a['Unnamed: 6'][a['Unnamed: 6'] == 0].index)
    a = a.drop(a['流动性数据'][a['流动性数据'] == 0].index)
    a = a.drop(a['Unnamed: 8'][a['Unnamed: 8'] == 0].index)
    # a = a.drop(a['Unnamed: 9'][a['Unnamed: 9'] == 0].index)

    return a


def total_time(a):
    bvalue = a['基本面数据']
    # print(bvalue)
    total = 0
    for i in bvalue:
        total = total + i
    # ave = total / len(bvalue)

    return total


def cal_lamda(list):
    lamda_list = []
    for i in range(0, 9):
        lamb = list[i] / list[i + 1]
        lamda_list.append(lamb)

    return lamda_list


def frame_get():
    list_ten1.reverse()
    year_list = []
    print(len(list_ten1))
    for i in range(2009, 2019):
        year_list.append(i)
    print(len(year_list))
    data = {'year': year_list,
            'total': list_ten1,
            }
    frame = pd.DataFrame(data)
    # print(frame)
    return frame


def draw():
    x = range(2009, 2019)
    y = list_ten1

    fig = pl.figure(figsize=(4, 4))
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y, c='red')
    pl.show()


def lsm():
    x_2 = []
    for i in year_list:
        x_2.append(i ** 2)

    xy_add = 0

    for i in range(0, 9):
        xy = list_ten1[i] * year_list[i]
        xy_add = xy_add + xy

    k = (10 * xy_add - sum(year_list) * sum(list_ten1)) / (10 * sum(x_2) - pow(sum(year_list), 2))
    b = (sum(list_ten1) / 10) - k*(sum(year_list) / 10)
    print(k)
    print(b)
    return k, b


def draw_line():
    x1 = year_list
    y1 = list_ten1

    fig = pl.figure(figsize=(4, 4))
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x1, y1, c='red')

    x = np.arange(2009, 2020)
    y = 2137561764872.7273 * x + -4282799219019227.5
    pl.plot(x, y)

    pl.show()


if __name__ == '__main__':
    # 路径
    path1 = 'D:\\learning\\math\\19C\\2019-51MCM-Problem C-Appendix 1.xls'
    path2 = 'D:\\learning\\math\\19C\\2019-51MCM-Problem C-Appendix 2.xlsx'

    list_ten1 = []
    for i in range(0, 10):
        a = pd.read_excel(path1, sheet_name=i)
        a = rush(a, '估值数据')
        total = total_time(a)
        list_ten1.append(total)

    # 算lamda,检验是否正确
    lambda_list = cal_lamda(list_ten1)
    for i in lambda_list:
        if ((i < np.e - 2) & (i > np.e - 4)):
            print('ok')

    frame = frame_get()

    year_list = []
    for i in range(2009, 2019):
        year_list.append(i)
    # 最小二乘
    draw()
    print(year_list)
    print(list_ten1)
    k, b = lsm()
    draw_line()
