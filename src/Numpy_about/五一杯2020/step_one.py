import numpy as np
import pandas as pd
from mpmath import ln

# path = 'C:\\Users\\86139\\Desktop\\汇总表.xlsx'
path = 'C:\\Users\\86139\\Desktop\\test.xlsx'
a = pd.read_excel(path)
print(a)
# print(a['煤炭生产量(万吨)'])
# list_index1 = [ '煤炭消费量（万吨）',
#                '大型煤炭交易市场数量（个）', 'GDP增速','煤炭生产量(万吨)' ]
# list_index2 = ['进口煤量(万吨)',  '大气CO2（十亿吨）','国际油价（元/桶）',
#                '火电装机增加量（亿千瓦小时）']
x_ij = []
list_index1 = ['消费量','产量2','进口','油价2','GDP']
list_index2 = []
count = 0
for j in list_index1:
    x_ij.append([])
    a[j] = a[j].dropna()
    # print(a[j])
    for i in range(0, 8):
        # print(a[j][len(a[j])])
        # print()
        # print(type(a[j][i]))
        x = (a[j][i] - a[j][8]) / (a[j][9] - a[j][8])
        x_ij[count].append(x)
    count = count + 1

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
print('===============================')

# 第j项指标下第i个样本值占该指标的比重
p_ij = []
for i in range(0, len(x_ij)):
    total = 0
    p_ij.append([])
    for j in x_ij[i]:
        total = total + j
    # print(total)
    for j in x_ij[i]:
        p = j / total
        p_ij[i].append(p)

print(p_ij)
# print(len(p_ij[0]))
print('============================')
# 第j指标的熵值

k = 1 / ln(len(p_ij[0]))
# print(k)

for i in range(0, len(p_ij)):
    for j in range(0, len(p_ij[i])):
        p_ij[i][j] += 0.00000001

# print(p_ij)
e_j = []
for i in range(0, len(p_ij)):
    e = 0
    for j in p_ij[i]:
        e = e + (j * ln(j))
    e = -k * e
    # print(e)
    # print('=================================')
    e_j.append(e)
# print(ln(0.013757470999100435) * 0.013757470999100435)
# 这边我直接一个个复制黏贴了，不知道为什么会有mpf的问题
# e_j = [0.91278033578989, 0.923923340301428, 0.860432585240335, 0.84537884679091, 0.871684128961821, 0.895531600360308,
#        0.926715212634005, 0.875912011894123]
print(e_j)
# 信息熵冗余度
d_j = []
for i in e_j:
    d_j.append(1 - i)
# 指标权重
print(d_j)
print(len(d_j))
w_j = []
total = 0
for i in d_j:
    total = total + i

for i in d_j:
    w = i / total
    w_j.append(w)
print(w_j)
# w_j.sort()

# print(sum(w_    j))
# 综合得分
# s_i = []
# a = pd.DataFrame(p_ij)
# print(a)
