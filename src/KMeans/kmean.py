from math import sqrt

def cal_distance(p1, p2):
    distance = pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)
    return distance

# 可以这么做输入数据，但是我懒就直接规定数据
# p1 = Point(float(input()), float(input()))
# p2 = Point(float(input()), float(input()))
# print(p1.cal_distance(p2))
# 一些实验数据




Xn = [[1, 0], [0.581831872, 0.813971794], [0.522831173, 0.814824533], [0.667724412, 0.742800918],
          [0.547141397, 0.822958347],
          [0.760205454, 0.853722532], [0.478836121, 0.840997048], [0, 1], [0.403350723, 0.785897015],
          [0.555961921, 0.897540177],
          [0.555827462, 0.897605772], [0.555693003, 0.897605772], [0.543134513, 0.893276484],
          [0.553568547, 0.892489341]]




# p1 = [1,	0]
# p2 = [0.581831872,	0.813971794]
# p3 = [0.522831173,	0.814824533]
#
# p4 = [0.667724412,	0.742800918]
# p5 = [0.547141397, 0.822958347]
# p6 = [0.760205454, 0.853722532]
#
# p7 = [0.478836121, 0.840997048]
# p8 = [0, 1]
# p9 = [3, 16]

# point_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
point_list = Xn
# 初始中心点
center1 = (1,0)
center2 = (0.58,0.81)
center3 = (0,1)
#迭代中心点
center_list_int = [center1, center2, center3]
center_list_new = [0,0,0]
# 簇
point_ass = [[], [], []]

#用map优化
# point_assemble = {}
# point_assemble = point_assemble.fromkeys(point_list,())
# print(point_assemble)
#迭代次序
num = 0
while True:
    num = num + 1
    # 算每个点到三个聚类点的距离，分类
    for i in point_list:
        distance_list = []
        for j in center_list_int:
            distance_list.append(cal_distance(i, j))

        index = 0
        for k in range(0, 3):
            if distance_list[k] == min(distance_list):
                index = k
        point_ass[index].append(i)
    # 把一个类中的取平均值，作为center
    # print(point_ass)
    for i in range(0, 3):
        total_x = 0
        total_y = 0
        for j in range(0, len(point_ass[i])):
            total_x = point_ass[i][j][0] + total_x
            total_y = point_ass[i][j][1] + total_y
        ave_x = total_x / 3
        ave_y = total_y / 3
        center_list_new[i] = [ave_x,ave_y]
    print(center_list_new)


    # 两个center相同时，不再计算这个点
    if center_list_int == center_list_new:
        # print(center_list_new)
        # print(num)
        break
    else:
        center_list_int = center_list_new
        center_list_new = [0,0,0]

print("中心点为")
print(center_list_new)
print("点的聚合分类")
for obj in point_ass:
    print(obj[0:3])

