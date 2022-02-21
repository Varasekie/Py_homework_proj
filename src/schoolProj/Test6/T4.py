class MyList:
    def __init__(self, lists):
        self.list = list(lists)

    # 重置add方法，可以将运算符的方法改变。
    def __add__(self, other):
        # returnList作为一个返回值，便于返回列表的每一项
        returnList = []
        # n为两个列表的长度的差
        n = len(self.list) - len(other.list)
        # 如果n>0,则self较长
        if n > 0:
            # 在n之内的，按下标相加
            for i in range(0, len(other.list)):
                returnList.append(self.list[i] + other.list[i])
            # 超过n的部分，就将最后的直接全部添加进去。
            for i in range(len(other.list), len(self.list)):
                returnList.append(self.list[i])
        # 如果n<=0,则other较长
        else:
            for i in range(0, len(self.list)):
                returnList.append(self.list[i] + other.list[i])
            for i in range(len(self.list), len(other.list)):
                returnList.append(other.list[i])
        return returnList


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 9))
L3 = L1 + L2
print(L3)
