# 输入处理
a = input("请输入一个整数（输入字符A时结束处理）")
list = []
while(a != 'A'):
    list.append(int(a))
    a = input("请输入一个整数（输入字符A时结束处理）")

# 计算奇数之和，利用列表表达式筛选奇数
list_odd = [i for i in list if i%2 ==1.0]
# 计算偶数之和，利用列表表达式筛选偶数
list_even = [i for i in list if i%2 ==0.0]
sum_odd = sum(list_odd)
sum_even = sum(list_even)
# 计算平均值
ave = (sum_odd+sum_even)/(len(list_even)+len(list_odd))
# 打印
print("所有奇数之和"+str(sum_odd))
print("所有偶数之和"+str(sum_even))
print("平均值"+str(ave))
