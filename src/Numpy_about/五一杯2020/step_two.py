import math

import numpy as np
import pandas as pd


path = 'C:\\Users\\86139\\Desktop\\附件1-秦皇岛港动力煤历史价格.xlsx'

a = pd.read_excel(path)
price_data = pd.read_excel(path)
price_data = price_data.dropna()
# print(price_data)
date_range = pd.date_range('2006-07-08', periods = 671, freq = '7D')
Wprice_avg_range = pd.Series(price_data['价格平均值(元/吨)'].values, index = date_range)
Yprice_avg_range = Wprice_avg_range.resample('Y').mean()
Mprice_avg_range = Wprice_avg_range.resample('M').mean()
Dprice_avg_range = Wprice_avg_range.resample('D').interpolate()
#
print('=================')

# print(Mprice_avg_range)
Mprice_avg_range = Mprice_avg_range[-5 : -1]
X0 = np.array(Mprice_avg_range.values)
X1_list = [sum(Mprice_avg_range[0:i+1]) for i in range(len(Mprice_avg_range))]
X1 = np.array(X1_list)
B = np.zeros([len(Mprice_avg_range)-1,2])
Y = np.zeros([len(Mprice_avg_range)-1,1])
for i in range(0,len(Mprice_avg_range)-1):
    B[i][0] = -0.5*(X1[i] + X1[i+1])
    B[i][1] = 1
    Y[i][0] = X0[i+1]
A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)

# print(A)
a = A[0][0]
b = A[1][0]
X_hat = np.zeros(len(Mprice_avg_range))
X_hat[0] = X0[0]
for i in range(1,len(Mprice_avg_range)):
    X_hat[i] = (X0[0] - b/a) * (1 - math.exp(a)) * math.exp(-a * (i))

# print(Mprice_avg_range)
print(X_hat)
#求残差平均值
epsilon = 0
for i in range(0,len(Mprice_avg_range)):
    epsilon += (X0[i] - X_hat[i])
epsilon /= len(Mprice_avg_range)
# print(epsilon)

#求历史数据平均值
aver = X0.mean()

#求历史数据方差
s12 = 0
for i in range(0,len(Mprice_avg_range)):
    s12 += (X0[i]-aver)**2
s12 /= len(Mprice_avg_range)
s22 = 0
for i in range(0,len(Mprice_avg_range)):
    s22 += ((X0[i] - X_hat[i]) - epsilon)**2
s22 /= len(Mprice_avg_range)
#后验差比值
C = s22 / s12
# print('#后验差比值')
# print(C)

#小误差概率
cout = 0
for i in range(0,len(Mprice_avg_range)):
    if abs((X0[i] - X_hat[i]) - epsilon) < 0.6754*math.sqrt(s12):
        cout = cout+1
    else:
        cout = cout
P = cout / len(Mprice_avg_range)
# print(P)
if (C <= 0.5 and P >= 0.75):
    m = 36
    f = np.zeros(m)
    for i in range(0,m):
        f[i] = (X0[0] - b/a)*(1-math.exp(a))*math.exp(-a*(i+len(Mprice_avg_range)))
else:
    print('灰色预测法不适用')

print('=================')

# Dprice_avg_range = Dprice_avg_range[-5 : -1]
# X0 = np.array(Dprice_avg_range.values)
# X1_list = [sum(Dprice_avg_range[0:i+1]) for i in range(len(Dprice_avg_range))]
# X1 = np.array(X1_list)
# B = np.zeros([len(Dprice_avg_range)-1,2])
# Y = np.zeros([len(Dprice_avg_range)-1,1])
# for i in range(0,len(Dprice_avg_range)-1):
#     B[i][0] = -0.5*(X1[i] + X1[i+1])
#     B[i][1] = 1
#     Y[i][0] = X0[i+1]
# A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
# a = A[0][0]
# b = A[1][0]
# X_hat = np.zeros(len(Dprice_avg_range))
# X_hat[0] = X0[0]
# for i in range(1,len(Dprice_avg_range)):
#     X_hat[i] = (X0[0] - b/a) * (1 - math.exp(a)) * math.exp(-a * (i))
#
# #求残差平均值
# epsilon = 0
# for i in range(0,len(Dprice_avg_range)):
#     epsilon += (X0[i] - X_hat[i])
# epsilon /= len(Dprice_avg_range)
#
# #求历史数据平均值
# aver = X0.mean()
#
# #求历史数据方差
# s12 = 0
# for i in range(0,len(Dprice_avg_range)):
#     s12 += (X0[i]-aver)**2
# s12 /= len(Dprice_avg_range)
# s22 = 0
# for i in range(0,len(Dprice_avg_range)):
#     s22 += ((X0[i] - X_hat[i]) - epsilon)**2
# s22 /= len(Dprice_avg_range)
# #后验差比值
# C = s22 / s12
# print('#后验差比值')
# print(C)
#
# #小误差概率
# cout = 0
# for i in range(0,len(Dprice_avg_range)):
#     if abs((X0[i] - X_hat[i]) - epsilon) < 0.6754*math.sqrt(s12):
#         cout = cout+1
#     else:
#         cout = cout
# P = cout / len(Dprice_avg_range)
# print(P)
# if (C <= 0.5 and P >= 0.75):
#     m = 36
#     f = np.zeros(m)
#     for i in range(0,m):
#         f[i] = (X0[0] - b/a)*(1-math.exp(a))*math.exp(-a*(i+len(Dprice_avg_range)))
# else:
#     print('灰色预测法不适用')
#
