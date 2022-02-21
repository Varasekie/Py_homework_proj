s = "语文：80，数学：82，英语：90，物理：85，化学：88，美术：80"
list = s.split("，")
dict = {}
# 以字典形式同时遍历，提取课程和分数。
for i in list:
    dict[i.split("：")[0]] = i.split("：")[1]
sum = 0
# 直接提取字典的值，先进行格式转化然后相加
for i in dict.values():
    sum = sum + int(i)
# 保留一位小数
mean = round(sum / len(dict),1)
print("总分：",'')
print(sum)
print("平均分：",'')
print(mean)