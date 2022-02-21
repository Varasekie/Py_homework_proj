# 暂时使用数组存储图形,感觉也挺好的（……）
class MapParser:
    row = 27
    maps = []

    # 准备三个列表，分别对应三个动作集，即路口和无法行动

    def __init__(self, list):
        # 加载初始
        self.maps = [[" "] * self.row for i in range(0, self.row)]
        # 保证list的路口没有在边界上的，否则导入失误
        for item in list:
            self.maps[item[0]][item[1]] = "*"
        for i in range(0, int(self.row)):
            self.maps[i][0] = "#"
            self.maps[0][i] = "#"
            self.maps[i][self.row - 1] = "#"
            self.maps[self.row - 1][i] = "#"

    def proposeMove(self, action):
        pass

    def actionList(self, toDoBlock):
        if toDoBlock == '#':
            return 0
        elif toDoBlock == " ":
            return 1
        else:
            return 2

    def getTransitionProbability(self, oldState, newState, action, gridWorld):
        proposedCell = gridWorld.proposeMove(action)
        if proposedCell is None:
            # Rule 1 and 2: illegal move
            return transitionProbabilityForIllegalMoves(oldState, newState)
        if oldState.isGoal():
            # Rule 4: stay at goal
            return 0
        if proposedCell != newState:
            # Rule 3: move not possible
            return 0
        else:
            # Rule 3: move possible
            return 1


list_his = [[7, 15],
            [3, 8], [3, 4]]
a = MapParser(list=list_his)
for i in range(0, 27):
    for j in range(0, 27):
        print(a.maps[i][j], end="")
    print()
