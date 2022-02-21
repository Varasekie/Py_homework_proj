class average():

    def ave(self, list):
        total = 0
        for i in range(0, len(list)):
            total = total + list[i]
        ave = total / len(list)
        # print(ave)
        return ave

    def plus_ave(self, list1, list2):
        total = 0
        for i in range(0, len(list1)):
            total = total + list1[i] * list2[i]

        ave = total / len(list1)
        # print(ave)
        return ave

    def pow_ave(self, list):
        total = 0
        for i in range(0, len(list)):
            total = total + pow(list[i], 2)

        ave = total / len(list)
        return ave


def     kb_cal(a, t):
    xy = average()
    xy_ave = xy.plus_ave(a, t)
    # print('xy的乘积的均值' )
    # print(xy_ave)

    x = xy.ave(t)
    # print("x的均值")
    # print(x)

    y = xy.ave(a)
    # print('y的均值')
    # print(y)

    x_pow = xy.pow_ave(t)
    # print('x的平方的均值')
    # print(x_pow)

    k = (xy_ave - x * y) / (x_pow - pow(x, 2))
    print('k的值')
    print(k)

    b = y - k * x
    print('b的值')
    print(b)


def inputlist():
    print('一共有多少个数：')
    num = int(input())
    # print(num)
    list1 = []
    for i in range(0, num):
        index = i + 1
        print("输入第%d个数" % index)
        list1.append(float(input()))

    return list1


def totmain():
    print('先输入x轴的数据')
    listx = inputlist()
    print('输入y轴的数据')
    listy = inputlist()
    kb_cal(listy, listx)


def list_ave():
    list = inputlist()
    listaver = average()
    ave = listaver.ave(list)
    print("平均值")
    print(ave)


def list_standard_deviation():
    total = 0
    list = inputlist()
    listaver = average()
    ave = listaver.ave(list)
    print("平均值")
    print(ave)
    for i in list:
        total = total + pow(ave - i, 2)
    print("标准差")
    print(pow(total / (len(list) - 1), 0.5))
    return pow(total / (len(list) - 1), 0.5), len(list)


def A_undefined():
    standard, len = list_standard_deviation()
    a_undefined = standard / pow(len, 0.5)
    print("a不确定度")
    print(a_undefined)
    return a_undefined


def B_undefined():
    print("B类仪器测量误差限为")
    b = input()
    b_undifined = float(b) / pow(3, 0.5)
    print("b不确定度")
    print(b_undifined)
    return b_undifined


def uc():
    ua = A_undefined()
    ub = B_undefined()
    uc = pow(pow(ua, 2) + pow(ub, 2), 0.5)
    print("uc不确定度")
    print(uc)


if __name__ == '__main__':
    # totmain()
    # list_ave()
    # list_standard_deviation()
    # A_undefined()
    # uc()
    list_x = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    list_y = [9667569965771.793, 13589629378390.596, 17420441393412.488, 19655957374931.496, 21469924023524.754, 22570522412559.438, 22102357548248.73, 24079582033522.44, 29111964036051.652, 32145997353677.938]
    kb_cal(list_y,list_x)