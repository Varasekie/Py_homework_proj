s = input("请输入某个字符串")
list = []
# 遍历输入的内容转化成ASCII码，直接append列表
for i in s:
    list.append(ord(i))
# 打印
print(list)