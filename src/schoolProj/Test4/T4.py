def m(n):
    # 如果是1，则返回1
    if n == 1:
        a = 1
    else:
        # 返回m（n-1），可以直接进行计算
        a = m(n - 1) + 1 / n
    return a


print(m(2))
print(m((10)))
print(m(100))
