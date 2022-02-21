# 初始化dict
dict = {"aa": "1003", "bb": "1011", "cc": "1045", "dd": "1047", "ee": "1051"}

# 第一种，字典的方法，如果在dict.keys()中，则说明可以输出，如果不在，就反复输入。
s = input("please input")
while s != "n":
    if s in dict.keys():
        print("对应的值为",dict[s])
        s = input("请继续输入，n退出")
    else:
        s = input("不在字典中,重新输入")


# 第二种方法，使用异常处理
def testWord(m):
    try:
        s = input(m)
        # a为了异常处理，能够跳入才创造的变量
        a = dict[s]
    except KeyError:
        # 利用递归，如果这里错误就一直输出错误
        testWord("错误，请继续输入")
    else:
        print("对应的值为",dict[s])


testWord("please input")
