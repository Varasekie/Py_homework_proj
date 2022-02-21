lst=[("triangle","shape"),("red","color"),("square","shape"),("yellow","color"),("green","color"),("circle","shape")]
# 列表生成式，来交换顺序。
l1 = [(i[1],i[0]) for i in lst]
l1.sort()
print(l1)

# 列表生成式，通过判定color，筛选出颜色
# 利用tuple去重
l2 = tuple([i[0] for i in lst if i[1] == 'color'])
l2 = list(l2)
print(l2)