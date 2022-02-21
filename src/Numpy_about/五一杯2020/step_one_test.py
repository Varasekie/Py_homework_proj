import pandas as pd
import numpy as np

path = 'C:\\Users\\86139\\Desktop\\汇总表.xlsx'

a = pd.read_excel(path)
# print(a['煤炭生产量(万吨)'])
list_index1 = ['GDP增速','大型煤炭交易市场数量（个）', '火电装机增加量（亿千瓦小时）','煤炭生产量(万吨)']
list_index2 = [ '国际油价（元/桶）', '大气CO2（十亿吨）','进口煤量(万吨)' ]
list_index = ['GDP增速','大型煤炭交易市场数量（个）', '煤炭生产量(万吨)','煤炭生产量(万吨)',
              '火电装机增加量（亿千瓦小时）','国际油价（元/桶）', '大气CO2（十亿吨）','进口煤量(万吨)']
# [ 7.99999995e+00  5.43925576e-08  1.02589882e-11  9.70990193e-15
#   1.01147260e-15 -7.47877577e-16 -1.59485572e-16 -4.87809738e-29]
#
# from scipy.stats import kstest
#
#
# def KsNormDetect(df, i):
#     # 计算均值
#     u = df[i].mean()
#     # 计算标准差
#     std = df[i].std()
#     # 计算P值
#     res = kstest(df, 'norm', (u, std))[1]
#     # 判断p值是否服从正态分布，p<=0.05 则服从正态分布，否则不服从。
#     if res <= 0.05:
#         print('该列数据服从正态分布------------')
#         print('均值为：%.3f，标准差为：%.3f' % (u, std))
#         print('------------------------------')
#         return 1
#     else:
#         return 0
#
#
# def OutlierDetection(df, ks_res, value):
#     # 计算均值
#     u = df[value].mean()
#     # 计算标准差
#     std = df[value].std()
#     if ks_res == 1:
#         # 定义3σ法则识别异常值
#         # 识别异常值
#         error = df[np.abs(df[value] - u) > 3 * std]
#         # 剔除异常值，保留正常的数据
#         data_c = df[np.abs(df[value] - u) <= 3 * std]
#         # 输出异常数据
#         print(error)
#         return error
#
#     else:
#         print('请先检测数据是否服从正态分布-----------')
#         return None
#
#
# if __name__ == '__main__':
#     # 创建数据
#     # data = [1222, 87, 77, 92, 68, 80, 78, 84, 77, 81, 80, 80, 77, 92, 86, 76, 80, 81, 75, 77, 72, 81, 72, 84, 86, 80,
#     #         68, 77, 87, 76, 77, 78, 92, 75, 80, 78, 123, 3, 1223, 1232]
#     # df = pd.DataFrame(data, columns=['value'])
#     for i in list_index1:
#         ks_res = KsNormDetect(a, i)
#         result = OutlierDetection(a, ks_res, i)
#         print(result)

# import pandas as pd
#
#
# # 正态分布
# # 3sigma准则 --->
# #  mean() - 3* std() ---下限
# #  mean() + 3* std() ---上限
#
# # 自实现3sigma 原则
#
# def three_sigma(ser):
#     """
#     自实现3sigma 原则
#     :param ser: 数据
#     :return: 处理完成的数据
#     """
#     bool_id = ((ser.mean() - 3 * ser.std()) <= ser) & (ser <= (ser.mean() + 3 * ser.std()))
#
#     # bool数组索引
#
#     # ser[bool_id]
#     print(ser.index[bool_id])
#     return ser.index[bool_id]
#
#
# # 使用detail 验证
# deatil = pd.read_excel(path)
#
# print(deatil.shape)
#
# # 调用3sigma原则，进行异常值过滤
# count = 0
# for i in list_index1:
#     count = count +1
#     index_name_list = three_sigma(deatil[i])
#     print('==================')
#
# for i in list_index2 :
#     count = count +1
#     index_name_list = three_sigma(deatil[i])
#     print('==================')
#
# deatil = deatil.loc[index_name_list, :]
#
# print(deatil.shape)


# print('=============================================================')
# 标准化数据
x_ij = []
count = 0
# for j in list_index1:
#     x_ij.append([])
#     a[j] = a[j].dropna()
#     # print(a[j])
#     for i in range(1, 15):
#         # print(a[j][len(a[j])])
#         # print(a[j][i])
#         x = (a[j][i] - a[j][15]) / (a[j][16] - a[j][15])
#         x_ij[count].append(x)
#     count = count + 1
#
# for j in list_index2:
#     x_ij.append([])
#     a[j] = a[j].dropna()
#     # print(a[j])
#     for i in range(1, 15):
#         # print(a[j][len(a[j])])
#         # print(a[j][i])
#         x = (a[j][16] - a[j][i]) / (a[j][15] - a[j][16])
#         x_ij[count].append(x)
#     count = count + 1
# print(x_ij)
# print(len(x_ij))
# print('===============================')


# [mpf('0.085860490258438046'),
# mpf('0.15751646698011521'), mpf('0.17450618982824181'), mpf('0.098436539655235814'),
# mpf('0.1430208866161477'), mpf('0.11790354683181237'), mpf('0.082709569487681642'),
# mpf('0.1400463103423274')]
# '煤炭消费量（万吨）',
# '大型煤炭交易市场数量（个）', 'GDP增速','煤炭生产量(万吨)' ]
# '进口煤量(万吨)', '国际油价（元/桶）', '大气CO2（十亿吨）',
#                '火电装机增加量（亿千瓦小时）']


# 协方差矩阵
#算平均值

# 标准化数据
def ave(list,j):
    total = 0
    for i in range(1,15):
        total = total + a[j][i]
    return total/14

for j in list_index:
    x_ij.append([])
    a[j] = a[j].dropna()
    # print(a[j])
    for i in range(1, 15):
        # print(a[j][len(a[j])])
        # print(a[j][i])
        x = a[j][i] - ave(a[j],j)
        x_ij[count].append(x)
    count = count + 1

x_ij_1 = []
count = 0
# print('===================')


for j in range(0,len(x_ij)):
    x_ij_1.append([])
    total = 0
    for i in range(1, len(x_ij[j])):
        # print(a[j][len(a[j])])
        total = total + pow(x_ij[j][i],2)
    for i in range(0, len(x_ij)):
        x = x_ij[j][i]/pow(total/7,0.5)
        x_ij_1[count].append(x)
    count = count + 1
# print(x_ij_1)

a = np.array(x_ij_1)
a = a.T
C = np.cov(a, rowvar=False)
# 相关系数矩阵
R = np.corrcoef(C)
# print(R)
# 特征值，特征向量
eigenvalue, featurevector = np.linalg.eig(R)

print("特征值：", eigenvalue)
print("特征向量：", featurevector)

