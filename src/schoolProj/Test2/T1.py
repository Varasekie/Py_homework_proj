# 直接列出固定的日期的月份
list1 = ["1", '3', '5', '7', '8', '10', '12']
list2 = ['4', '6', '9', '11']
# flag作为控制跳出循环的变量
flag = True


# 自定义函数判断是否为闰年
def isLeapYear(year):
    return (int(year) % 400 == 0) | (int(year) % 100 != 0) & (int(year) % 4 == 0)


while (flag):
    year = input("请输入年份")
    month = input("请输入月份")
    # 使用list的自带函数，判断大小约
    if month in list1:
        print("该月有31天")
    elif month in list2:
        print("该月有30天")
    # 判断2月
    elif (month == '2') & isLeapYear(year):
        print("该月有29天")
    else:
        print("该月有28天")

    # 跳出循环的判断
    flags = input("是否继续查询y/n") == 'y'
    if flags == 'n':
        flag = False
