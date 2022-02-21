from matplotlib import pyplot as plt

y0 = [23092.36, 29599.31, 32191.3, 34938.24, 37002.16, 40471.79, 44552.83, 49935.9, 54259.2]
y1 = [23092, 32230, 37600, 43880, 51200, 59750, 69720, 81350, 94930]

x0 = range(2010,2019)
x1 = x0

# plt.plot(x0,y0)
# plt.plot(x1,y1)
# plt.show()

plt.scatter(x0,y0,marker="v")
plt.xlabel("year")
plt.ylabel("GDP")
plt.scatter(x1,y1,marker="s")
plt.legend(["predict","raw"])
plt.show()


