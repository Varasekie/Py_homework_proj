from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

"""
线性回归
"""
# 1.获取数据
boston = load_boston()  # 获取波士顿房价的数据


# # 2.训练模型
# model2 = LinearRegression().fit(x, y)
#
# # 3.模型预测
# pre = model2.predict(x)
#
# # 4.绘制结果
# plt.scatter(x, y, color='red')
# plt.plot(x, pre)
# plt.show()
# plt.close()

import numpy as np
import matplotlib.pyplot as plt
"""
利用 Python 实现线性回归模型
"""
class LinerRegressionModel(object):
    def __init__(self, data):
        self.data = data
        self.x = data[:, 0]
        self.y = data[:, 1]

    def log(self, a, b):
        print("计算出的线性回归函数为:\ny = {:.5f}x + {:.5f}".format(a, b))

    def plt(self, a, b):
        plt.plot(self.x, self.y, 'o', label='data', markersize=10)
        plt.plot(self.x, a * self.x + b, 'r', label='line')
        plt.legend()
        plt.show()

    def least_square_method(self):
        """
        最小二乘法的实现
        """
        def calc_ab(x, y):
            sum_x, sum_y, sum_xy, sum_xx = 0, 0, 0, 0
            n = len(x)
            for i in range(0, n):
                sum_x += x[i]
                sum_y += y[i]
                sum_xy += x[i] * y[i]
                sum_xx += x[i]**2
            a = (sum_xy - (1/n) * (sum_x * sum_y)) / (sum_xx - (1/n) * sum_x**2)
            b = sum_y/n - a * sum_x/n
            return a, b
        a, b = calc_ab(self.x, self.y)
        self.log(a, b)
        self.plt(a, b)


x = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [2.98, 2.9, 3.1, 3.3, 3.2, 3.2, 3.24, 3.25, 3.34, 3.3]
# data = np.array([[3, 2.98], [4, 2.9], [5, 3.1],[6, 3.3], [7, 3.2], [8, 3.2],[9,3.24],[10,3.25],[11,3.34],[12,3.3]])

# data = np.array([[1,3350],[2,1764],[3,2348],[4,2530],[5,2747],[6,2710],[7,3289],[8,3295],[9,3029],[10,2569],[11,2078]])
# 3.6 2.9 3.5 3.45 3.45 3.45 3.75 3.75 3.6 3.6

data = np.array([[1,3.6],[3,3.5],[4,3.45],[5,3.45],[6,3.45],[7,3.75],[8,3.75],[9,3.6],[10,3.6],[11,3.7]])
model = LinerRegressionModel(data)

model.least_square_method()
