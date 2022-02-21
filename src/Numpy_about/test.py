import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


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

    return avalue, a


def average(a, avalue):
    frameBin = [0, 2, 4, 6, 8, 10]
    # 按照0，2，4，6，8，10这样的区间切分
    f = pd.cut(avalue, frameBin)
    f = f.dropna()

    # 提取列表的索引
    index_list = f.index
    # print(index_list)

    # 把不同的区间扔进不同列表，并计数每个列有多少个
    num_list = [0, 0, 0, 0, 0]
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    for i in f.index:
        if (int(str(f[i])[4:-1]) == 2):
            list1.append(i)
            num_list[0] = num_list[0] + 1
        if (int(str(f[i])[4:-1]) == 4):
            list2.append(i)
            num_list[1] = num_list[1] + 1

        if (int(str(f[i])[4:-1]) == 6):
            list3.append(i)
            num_list[2] = num_list[2] + 1

        if (int(str(f[i])[4:-1]) == 8):
            list4.append(i)
            num_list[3] = num_list[3] + 1

        if (int(str(f[i])[4:-1]) == 10):
            list5.append(i)
            num_list[4] = num_list[4] + 1

    # 做平均值，五个区间五个值
    List = [list1, list2, list3, list4, list5]
    ave_list = []
    for j in List:
        total = 0
        num = 0
        for i in j:
            total = total + avalue[i]
            num = num + 1
        ave = total / num
        ave_list.append(ave)
        # print(ave)
    # print('===========================================')
    # print(num_list[0])
    # 算p/s，公式
    ps_list = []
    index = 0
    N = len(a)
    add = 0
    # print(N)
    for i in ave_list:
        add = i * num_list[index] + add
        index = index + 1
    ps = float(add) / float(N)

    # 十年的数据p/s数据返回一个列表
    return ps


def Bi(a, Bave_list):
    bvalue = a['基本面数据']
    # print(bvalue)
    total = 0
    for i in bvalue:
        total = total + i
    ave = total / len(bvalue)

    return ave


def vl(i, ps_list1, Bave_list):
    ave = ps_list1[i] * Bave_list[i] / Bave_list[i + 1]
    # print(ave)
    return ave


def tenStandard():
    # print(str(i) + 'year的每个指标均值是')
    # print(a['基本面数据'])
    ave_total = []
    aveten_list = []
    ave = 0
    list = ['基本面数据', 'Unnamed: 5', 'Unnamed: 6', '流动性数据', 'Unnamed: 8', 'Unnamed: 9']
    # 六个数据每一年的均值
    for j in list:
        ave_list = []
        total = 0
        length = 0
        for i in range(0, 10):
            # 十年数据
            a = pd.read_excel(path1, sheet_name=i)
            avalue, a = rush(a, '估值数据')
            # print(a[j])
            for k in a[j]:
                # print(k)
                if (type(k) == str):
                    continue
                total = total + k
                length = len(a[j]) + length
            ave = total / length
            ave_list.append(ave)
        ave_total.append(ave_list)
        # 十年的均值,6个数
        total = 0
        for i in ave_list:
            total = total + i
        ave = total / 10
        aveten_list.append(ave)
        # print(ave)
    # print(ave_list)
    # print(aveten_list)
    # print(ave_total)

    sd_list = []
    for j in list:
        num = 0
        ave_list = []
        total = 0
        length = 0
        for i in range(0, 10):
            a = pd.read_excel(path1, sheet_name=i)
            avalue, a = rush(a, '估值数据')
            for k in a[j]:
                if (type(k) == str):
                    continue
                total = pow(k - ave_total[num][i], 2) + total
                length = len(a[j]) + length
        anov = total / length
        sd = pow(anov, 0.5)
        sd_list.append(sd)
        num = num + 1
    # print(sd_list)

    x_list = [[], [], [], [], [], []]
    num = 0
    for i in ave_total:
        for j in i:
            if (num > 6):
                print('wrong')
            x = (j - aveten_list[num]) / sd_list[num]
            x_list[num].append(x)
        num = num + 1
    # print(x_list)
    # print('=========================================')
    return x_list


def cov_cal(x_list):
    a = np.array(x_list)
    a = a.T
    # print(type(a))
    # 相关系数矩阵
    b = np.cov(a, rowvar=False)
    print('相关系数矩阵')
    print(b)
    print('=========================================')

    # 特征值，特征向量
    eigenvalue, featurevector = np.linalg.eig(b)

    print('特征值，特征向量')
    print(eigenvalue)
    print(featurevector)
    print('=========================================')
    pca = PCA(n_components='mle')
    pca.fit(b)
    print(pca.explained_variance_ratio_)


if __name__ == '__main__':
    # 路径
    path1 = 'D:\\learning\\math\\19C\\2019-51MCM-Problem C-Appendix 1.xls'
    path2 = 'D:\\learning\\math\\19C\\2019-51MCM-Problem C-Appendix 2.xlsx'

    path3 = 'D:\learning\19\data\people.xlsx'
    # step1
    ps_list1 = []
    ps_list2 = []
    Bave_list1 = []
    Bave_list2 = []
    vl_list = []

    # pca
    a = pd.read_excel(path3)
    # ps_list = average(a,avalue=avalue)
    # 读文件,拿到p/s的值
    for i in range(0, 10):
        a = pd.read_excel(path1, sheet_name=i)
        # 拿到十年p/s的值
        avalue, a = rush(a, '估值数据')
        # print(avalue)
        ps_list = average(a, avalue=avalue)
        ps_list1.append(ps_list)
        # print(ps_list1)
        # 获得Bi的值
        Bave_list = Bi(a, Bave_list1)
        Bave_list1.append(Bave_list)
        # #算出vl
    # print(ps_list1)
    # print('================================')
    # print(Bave_list1)
    for i in range(0, 1):
        vl_list1 = vl(i, ps_list1, Bave_list1)
        vl_list.append(vl_list1)

    # 返回一个x_list
    # step2
    x_list = tenStandard()
    # print(x_list)
    # cov_cal(x_list)

    # for i in range(0, 10):
    #     a = pd.read_excel(path2, sheet_name=i)
    #     # 拿到十年p/s的值
    #     avalue = rush(a, '估值指标')
    #     ps_list2 = average(a, avalue=avalue)
    # # print('国外数据')
    # print(ps_list2)

    # step2
    # for i in range(0, 10):
    #     a = pd.read_excel(path1, sheet_name=i)
    #     avalue, a = rush(a, '估值数据')
    #     tenStandard(a, 2018 - i)
