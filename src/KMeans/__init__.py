p1 = [1, 1]
p2 = [3, 2]
p3 = [2, 1]

p4 = [9, 7]
p5 = [8, 9]
p6 = [10, 11]

p7 = [5, 14]
p8 = [4, 18]
p9 = [3, 16]
point_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

center1 = (1, 1)
center2 = (10, 10)
center3 = (3, 18)
center_list_int = [center1, center2, center3]
center_list_new = [0,0,0]
point_ass = [[], [], []]
point_list = set(point_list)
print(point_list)
#用map优化
point_assemble = {}
point_assemble = point_assemble.fromkeys(set(point_list),())
print(point_assemble)
# from math import sqrt
#
# print(sqrt(3) * 78 / 3)
# print(sqrt(3) * 172 / 3)
# print((26.41+25.56+26.12)/3)
# print((pow(166.36,2)+pow(191.56,2)) * 0.386 /8)

# import numpy as np
# list = [[1,2],[1,2]]
# a = np.mat(list)
# print(a)

# a = np.mat('1,2,3')
# b = np.mat('3,2')
# k = np.dot(b.T,a)
# print(k)
# print(b)
# k = np.dot(b.T,a.T)
# print(k)