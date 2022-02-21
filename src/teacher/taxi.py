class taxi:
    # 出租车可选的路的集合
    A = [0, 1, 2, 3]

    def __init__(self, location):
        self.location = location
        # 搭载状态
        self.take = True


from pylab import *  # 支持中文

mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['0.8', '0.825', '0.85', '0.875', '0.9', '0.925', '0.95', '0.975']
x = range(len(names))
y = [0.142857143, 0.143, 0.285714286, 0.32, 0.428571429, 0.571428571, 0.65, 0.714285714]
y1 = [0 for i in names]
y2 = [1 for i in names]
y3 = [1 / 13, 2 / 14,  0.2, 12/36, 12/36,13/36,14 / 36, 17 / 36]
# plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
# pl.xlim(-1, 11)  # 限定横轴的范围
# pl.ylim(-1, 110)  # 限定纵轴的范围


# plt.plot(x, y, marker='o', mec='*', mfc='w',label=u'key metric')
plt.plot(x, y1, marker='*', ms=5, label=u'DP')
plt.plot(x, y1, marker='d', ms=5, label=u'MDP_TAXI')
plt.plot(x, y, marker='o', ms=5, label=u'MDP_DP_TAXI')
plt.plot(x, y2, marker='v', ms=5, label=u'PDP')
# plt.plot(x, y3, marker='^', ms=5, label=u'MDP_DP_TAXI')

plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"Data Utility Requirement")  # X轴标签
plt.ylabel("Data Utility")  # Y轴标签
# plt.title("plot of data  ")  # 标题

plt.show()
