N = 330239523
# 人口总数
I = 5063561
E = I * 0.05
# 潜伏者
# % 传染者
S = N - I
# % 易感者
R = 7808059
# % 康复者

r = 5
# % 感染者接触易感者的人数
B = 0.006
# % 传染概率
a = 0.1
# % 潜伏者转化为感染者概率
r2 = 2
# % 潜伏者接触易感者的人数
B2 = 0.003
# % 潜伏者传染正常人的概率
y = 0.1
T = range(1,300)
for idx in range(1,300):
    if idx >= 10:
        r = 5
        r2 = 5

#     S(idx + 1) = S(idx) - r * B * S(idx) * I(idx) / N(1) - r2 * B2 * S(idx) * E(idx) / N;
#     E(idx + 1) = E(idx) + r * B * S(idx) * I(idx) / N(1) - a * E(idx) + r2 * B2 * S(idx) * E(idx) / N;
#     I(idx + 1) = I(idx) + a * E(idx) - y * I(idx);
#     R(idx + 1) = R(idx) + y * I(idx);
#
# end
# plot(T, S, T, E, T, I, T, R);
# grid
# on;
# hold
# on
# plot([10 10], [0 10000])
# xlabel('天')
# ylabel('人数')
# legend('易感者', '潜伏者', '传染者', '康复者', '执行戒严措施')
# title('戒严措施对SEIR模型的影响')