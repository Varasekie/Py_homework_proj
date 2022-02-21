dicStus = {'张三': ('男', 19), '李四': ('女', 18), '王五': ('男', 18),
           '赵六': ('女', 20), '徐伟伟': ('女', 19), '韩亮亮': ('女', 19)}
# 方法一
# 男生,女生的数量
# 利用列表表达式，直接筛选
man = [i for i in dicStus if dicStus[i][0]== '男']
woman = [i for i in dicStus if dicStus[i][0]== '女']
print("男生的数量是"+str(len(man)))
print("女生的数量是"+str(len(woman)))
over_18 = [i for i in dicStus if dicStus[i][1]> 18]
print("其中年龄超过18的有"+str(over_18))

# 方法二，遍历，然后设置变量来读写该变量。
# man_num = 0
# woman_num = 0
# over_18s = 0
# for i in dicStus.values():
#     if i[0] == '男':
#         man_num = man_num + 1
#     else:
#         woman_num = woman_num + 1
#     if i[1] > 18:
#         over_18s = over_18s + 1
