# 输入
a = int(input("请输入a，n的值"))
n = int(input())
sum = 0
item = a

# 方法一
# 每个的下一项为item*10+a
# for i in range(0, n):
#     sum = sum + item
#     item = item * 10 + a

# 方法二
# 利用数值转化
for i in range(1,n+1):
    sum = sum + int(str(a)*i)

print("值为:"+str(sum))
