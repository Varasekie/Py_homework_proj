import numpy as np
import pandas as pd

path = 'C:\\Users\\86139\\Desktop\\煤炭.xlsx'
a = pd.read_excel(path)
print(a)
list_index = ['热值（kcal/kg）','灰分（%）','挥发分（%）','硫分']
# 标准化数据
x_ij = []
count = 0
for j in list_index:
    x_ij.append([])
    # print(a[j])
    for i in range(0, 13):
        x = (a[j][i] - a[j][15]) / (a[j][14] - a[j][15])
        x_ij[count].append(x)
    count = count + 1
# 协方差矩阵
a = np.array(x_ij)
a = a.T
C = np.cov(a,rowvar=False)
# 相关系数矩阵
R = np.corrcoef(C)
#特征值，特征向量
eigenvalue, featurevector = np.linalg.eig(R)
print("特征值：", eigenvalue)
print("特征向量：", featurevector)
eigenvalue.sort()
print(eigenvalue)
total = 0
for i in eigenvalue:
    total = total + i
a = 2.90640928e+00/total
print(a)
