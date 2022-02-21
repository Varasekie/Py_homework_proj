
s= '''Whether the weather be fine, or whether the 
weather be not. Whether the weather be cold, or whether the 
weather be hot. We will weather the weather whether we like it or 
not.'''
s = s.lower()
s = s.replace('.','')
s = s.replace('\n','')
s = s.replace(',','')
dict = {}
s1 = s.split(" ")
# 用字典直接遍历，一次遍历降低复杂度
set = set(s1)
# print(set(s1))
for i in set:
    dict[i] = s.count(i)
print(dict)

