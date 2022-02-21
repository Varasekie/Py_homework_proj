def isdiff1(n):
    # 使用flag来判断是否需要退出循环
    flag = True
    n = str(n)
    # 调用字符串的count方法，获得某个字母出现的次数
    for i in n:
        if n.count(i) > 1:
            flag = False
            break
    # 控制输出是相同还是有重复
    print("各不相同") if flag else print("有重复数字")

# 第二种方法
def isdiff2(n):
    flag = True
    len_1 = len(n)
    # len_1保存一开始的长度，然后将n变成集合
    n = set(n)
    # 如果集合前后长度不同，则有重复的数字
    if len_1 != len(n):
        flag = False
    # 控制输出是相同还是有重复
    print("各不相同") if flag else print("有重复数字")


n = input("请输入一个正整数")
isdiff1(n)
# isdiff2(n)
