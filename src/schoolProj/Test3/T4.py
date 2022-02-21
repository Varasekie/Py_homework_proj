set1 = {'李雷', '张玉', '王晓刚', '陈红静', '方向', '司马清'}
set2 = {'施然', '李芳芳', '刘潇', '方向', '孙一航', '黄煌'}
set3 = {'陈红静', '方向', '刘培良', '张玉', '施小冉', '司马清'}
# 班级总人数
total_num = 25
# question1
num_all = len(set1.union(set2).union(set3))
print("没有选修课程的人数为" + str(total_num - num_all))
# question2
# 计算两两交集，再减去三个都修的
num_2 = len(set1.intersection(set2)) + len(set2.intersection(set3)) + len(set3.intersection(set1)) \
        - len(set1.intersection(set2).intersection(set3))
print("同时选修了两门课" + str(num_2))
# 计算三个的交集
num_3 = len(set1.intersection(set2).intersection(set3))
print("同时选修了三门课" + str(num_3))
# 修了一个门课 = 总修人数-修了两门课-修了三门课
num_1 = num_all - num_2 - num_3
print("只选修了一门课" + str(num_1))
