s = "When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the Powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
# 预处理
s.lower()
# 去掉标点
s_change = ''
a = s.split(',')  # 去除逗号
for i in range(0, len(a)):
    s_change = s_change + a[i]
# 去除句号
a = s_change.split('.')
s_change = ''
for i in range(0, len(a)):
    s_change = s_change + a[i]

# 对文本中的单词进行提取，生成一个列表
word = s_change.split(' ')
# 遍历列表，对列表中的元素进行统计。统计结果存放在字典中，键表示单词，值表示次数
dict = {}
for i in word:
    if dict.__contains__(i):
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
# 对字典进行排序，其中，将其变成元组，再对元组进行排序。由于元组默认是对第一项排序，我将顺序变化了
s = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
print("单词的词频统计为")
print(dict)
print("前五的词频为" + str(s[:5]))