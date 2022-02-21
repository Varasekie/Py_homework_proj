# 历史数据
import random
import numpy as np

# 一、随机生成历史数据
# 都是简化的！想复杂是可以复杂的！的
# list_his = []
# for i in range(0,27):
#     x = int(random.random()*100)
#     y = int(random.random()*100)
#     list_his.append([x,y])
#
# print(list_his)
# 先直接用带入，后期当然可以更改
list_his = [[51, 2], [2, 52], [64, 21], [45, 66], [32, 1], [36, 38], [67, 47], [14, 75], [67, 81], [7, 15], [49, 61],
            [83, 5], [47, 9], [92, 91], [88, 77], [71, 31], [0, 88], [52, 90], [22, 88], [61, 36], [81, 65], [94, 21],
            [29, 60], [33, 87], [3, 8], [62, 79], [0, 4]]
# 添加噪声，b=1.μ = 0
list_his_DP = list_his
print(list_his)

# 二、随机生成司机当前数据
# 当前driver的地址，如果只有一个driver的推荐
driver_loc = [13, 10]

# 三、随机生成乘客的当前数据
# list_pass = []
# for i in range(0, 5):
#     x = int(random.random() * 100)
#     y = int(random.random() * 100)
#     list_pass.append([x, y])
# print(list_pass)
list_pass = [[49, 52], [98, 72], [39, 32], [48, 14], [50, 46]]
list_pass_DP = list_pass
# 四、给所有的当前乘客和历史数据方位进行DP
# 在中央处理之前进行DP操作，实现LDP
# 给driver当前位置添加DP
b = 1
μ = 0
driver_loc = [(1 / (2 * b)) * np.e ** (-1 * (np.abs(item - μ) / b)) for item in driver_loc]

# print(driver_loc)
# 给当前的乘客位置、历史数据做LDP
for item in list_pass_DP:
    item[0] = (1 / (2 * b)) * np.e ** (-1 * (np.abs(item[0] - μ) / b))
    item[1] = (1 / (2 * b)) * np.e ** (-1 * (np.abs(item[1] - μ) / b))

for item in list_his_DP:
    item[0] = (1 / (2 * b)) * np.e ** (-1 * (np.abs(item[0] - μ) / b))
    item[1] = (1 / (2 * b)) * np.e ** (-1 * (np.abs(item[1] - μ) / b))
his_pass = [0, 0, 0, 0]  # 历史记录，由于是推荐方位，只需要给出上下左右便可，此处指考虑了十字路口
# print(list_DP)
# print(list_pass_DP)
for item in list_his_DP:
    # 计算上下左右四个，此时的斜切角,  item是历史的。driver是当前的
    # 画个图就能理解了，本质将整个坐标系划成8块
    if ((item[1] - driver_loc[1]) / (item[0] - driver_loc[0])) > 0:
        if ((item[1] - driver_loc[1]) / (item[0] - driver_loc[0])) > 1:
            if (item[1] - driver_loc[1]) > 0:
                his_pass[0] = his_pass[0] + 1
            else:
                his_pass[1] = his_pass[1] + 1
        else:
            if (item[1] - driver_loc[1]) > 0:
                his_pass[3] = his_pass[3] + 1
            else:
                his_pass[2] = his_pass[2] + 1
    else:
        if ((item[1] - driver_loc[1]) / (item[0] - driver_loc[0])) < -1:
            if (item[1] - driver_loc[1]) > 0:
                his_pass[0] = his_pass[0] + 1
            else:
                his_pass[1] = his_pass[1] + 1
        else:
            if (item[1] - driver_loc[1]) > 0:
                his_pass[3] = his_pass[3] + 1
            else:
                his_pass[2] = his_pass[2] + 1
print(his_pass)


# [4, 18, 3, 2],无论是否进行DP处理都是这样,没影响最后的结果

# 以下开始MDP

# for item in his_pass:
# 此处写policy_allow是为了后期如果需要处理三岔路口则如何进行运作
class policy:
    # policy指的是三路口、
    policy = {}
    def policy_allow(self, action, section):

        if len(self.policy) ==0:
            # 当没有限制的时候，就尝试所有的try
            return 0
        if not section:
            # 此处return0表示限制了一部分行动（即只有三个路口）
            return 0
        else:
            return 1

    def transitionProbabilityForIllegalMoves(self,oldState, newState):
        return 0
    def getTransitionProbability(self, oldState, newState, action, gridWorld):

        proposedCell = gridWorld.proposeMove(action)
        if proposedCell is None:
            # Rule 1 and 2: illegal move
            return self.transitionProbabilityForIllegalMoves(oldState, newState)
        if oldState.isGoal():
            # Rule 4: stay at goal
            return 0
        if proposedCell != newState:
            # Rule 3: move not possible
            return 0
        else:
            # Rule 3: move possible
            return 1

