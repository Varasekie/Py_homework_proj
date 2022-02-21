import numpy as np
# path = r'D:\p\data\data.csv'
# f1 = open(r'D:\p\data\data1.txt')
# b = 2
# μ = 0
# # 将所有的分成10个类，对应操作系统的10个优先级，其中用户所选择的，然后从低到高和为1嘛，对吧，然后我认为设定，10个等级分别是1-10
#
# with open (path,'r',encoding='gb18030') as f:
#     a = f.readline()
#     for a in f.readlines():
#         list = a.split(',')
#         origin = float(list[-2])
#         DP = (1 / (2 * b)) * np.e ** (-1 * (np.abs(origin - μ) / b))
#         print(str(DP))

# query_result = 0
# for i in range(1,11):
#     query_result = query_result +i
# n=1
# loc = 0
# noise = 0
# for i in range(0,1000000):
#     noise = noise + abs(np.random.laplace(loc, scale=1/n, size=1))  # 从参数为（loc, scale）的拉普拉斯分布中随机抽取1个样本，返回数组类型的变量noise
# print(noise/1000000)



# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0', '0.5', '1', '1.5', '2','2.5','3','3.5']
x = range(len(names))
y = [0.42, 0.44, 0.44, 0.46, 0.47,0.49,0.5,0.5]
# y1=[0.86,0.85,0.853,0.849,0.83]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围


# plt.plot(x, y, marker='o', mec='*', mfc='w',label=u'key metric')
plt.plot(x, y, marker='*', ms=10,label=u'MSE(key metric)')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"μ") #X轴标签
plt.ylabel("MSE(key metric)") #Y轴标签
plt.title("plot of privacy cost") #标题

plt.show()

