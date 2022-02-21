import numpy as np
import pandas as pd

path = 'C:\\Users\\86139\\Desktop\\汇总表.xlsx'

a = pd.read_excel(path)
# print(a['煤炭生产量(万吨)'])
list_index1 = [ '煤炭消费量（万吨）','火电装机增加量（亿千瓦小时）',
               '大型煤炭交易市场数量（个）', 'GDP增速', ]
list_index2 = [ '国际油价（元/桶）', '大气CO2（十亿吨）','进口煤量(万吨)'
               ]

x_ij = []
# count = 0
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
datas = pd.read_excel('C:\\Users\\86139\\Desktop\\汇总表.xlsx')

datas = datas.dropna()

# price_avg = pd.Series(datas['价格平均值(元/吨)'].values)
coal_product = pd.Series(datas['煤炭生产量(万吨)'].values)
coal_import = pd.Series(datas['进口煤量(万吨)'].values)
coal_consumption = pd.Series(datas['煤炭消费量（万吨）'].values)
crude_oil = pd.Series(datas['国际油价（元/桶）'].values)
heat_energy = pd.Series(datas['火电装机增加量（亿千瓦小时）'].values)
coal_market = pd.Series(datas['大型煤炭交易市场数量（个）'].values)
gdp = pd.Series(datas['GDP增速'].values)
CO2 = pd.Series(datas['大气CO2（十亿吨）'].values)

# nprice_avg = np.array(price_avg)
ncoal_product = np.array(coal_product)
ncoal_import = np.array(coal_import)
ncoal_consumption = np.array(coal_consumption)
ncrude_oil = np.array(crude_oil)
nheat_energy = np.array(heat_energy)
ncoal_market = np.array(coal_market)
ngdp = np.array(gdp)
nCO2 = np.array(CO2)

# nprice_avg = ((np.max(nprice_avg) - nprice_avg) / (np.max(nprice_avg) - np.min(nprice_avg))) + 0.0001
ncoal_product = ((ncoal_product - np.min(ncoal_product)) / (np.max(ncoal_product) - np.min(ncoal_product))) + 0.0001
ncoal_import = ((np.max(ncoal_import) - ncoal_import) / (np.max(ncoal_import) - np.min(ncoal_import))) + 0.0001
ncoal_consumption = ((ncoal_consumption - np.min(ncoal_consumption)) / (np.max(ncoal_consumption) - np.min(ncoal_consumption))) + 0.0001
ncrude_oil = ((np.max(ncrude_oil) - ncrude_oil) / (np.max(ncrude_oil) - np.min(ncrude_oil))) + 0.0001
nheat_energy = ((nheat_energy - np.min(nheat_energy)) / (np.max(nheat_energy) - np.min(nheat_energy))) + 0.0001
ncoal_market = ((ncoal_market - np.min(ncoal_market)) / (np.max(ncoal_market) - np.min(ncoal_market))) + 0.0001
ngdp = ((ngdp - np.min(ngdp)) / (np.max(ngdp) - np.min(ngdp))) + 0.0001
nCO2 = ((np.min(nCO2) - nCO2) / (np.max(nCO2) - np.min(nCO2))) + 0.0001

datas = pd.DataFrame([ ncoal_product, ncoal_import, ncoal_consumption, ncrude_oil, nheat_energy, ncoal_market, ngdp, nCO2])
datas = pd.DataFrame(datas.values.T, index=datas.columns, columns=datas.index)


# 协方差矩阵
a = np.array(datas)
# a = a.T
C = np.cov(a, rowvar=False)
# 相关系数矩阵
R = np.corrcoef(C)
# 特征值，特征向量
eigenvalue, featurevector = np.linalg.eig(R)

print("特征值：", eigenvalue)
print("特征向量：", featurevector)

# total = 0
# for i in eigenvalue:
#     total = total + i
#
# list = []
# for i in eigenvalue:
#     l = i / total
#     list.append(l)
# print(list)
