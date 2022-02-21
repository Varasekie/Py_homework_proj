import matplotlib
import numpy as np
import matplotlib.pyplot as plt

path = "data.csv"
# 使用numpy读取csv文件
# 1）	统计股价近期最高价的最大值，最低价的最小值
maxPrice = np.loadtxt(path, delimiter=',', usecols=4, unpack=True, skiprows=0)
print(max(maxPrice))
lowPrice = np.loadtxt(path, delimiter=',', usecols=5, unpack=True, skiprows=0)
print(min(lowPrice))
# 2）	计算股价近期最高价的极差和最低价的极差（极差：最大值和最小值的差值），
print(np.ptp(maxPrice))
print(np.ptp(lowPrice))
# 3）	计算收盘价的中位数
closingPrice = np.loadtxt(path, delimiter=',', usecols=6, unpack=True, skiprows=0)
print(np.median(closingPrice))
print(np.var(closingPrice))

# 接下来是画图
# 这一句是显示中文
matplotlib.rcParams['font.family'] = 'FangSong'
# date作为横轴
date = np.loadtxt(path, delimiter=',', usecols=1, unpack=True, skiprows=0, dtype=str)
# 开盘价作为纵轴
openingPrice = np.loadtxt(path, delimiter=',', usecols=3, unpack=True, skiprows=0)
plt.subplot(211)  # 画上面一块
plt.plot(date, openingPrice)  # 分别画三条曲线
plt.plot(date, maxPrice)
plt.plot(date, lowPrice)
plt.plot(date, closingPrice)
# 设置45度倾斜
plt.xticks(date, rotation=45)
# 画图例
plt.legend(['开盘价', "最高价", '最低价', '收盘价'])
# 画第二张图
plt.subplot(212)
deal = np.loadtxt(path, delimiter=',', usecols=7, unpack=True, skiprows=0)
plt.plot(date, deal)
plt.xticks(date, rotation=45)
# 显示图
plt.show()
