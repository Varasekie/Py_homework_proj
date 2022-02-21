import random
# 导入一下
# 创建一些数据。（使用随机生成+人工调整）
from Py_homework_proj.src.teacher.road import road

p1 = [118.836696, 31.915403]
p2 = [118.837307, 31.900629]


# 大概思路：图存储，图会读取一个矩阵，根据矩阵来存储。
# 矩阵的生成通过一个接口
# 假设整个路段是长方形的，start和end是边长
# 本质来说，暂时不用考虑图的添加。因为建造路是低频率事件。邻接矩阵存储图。此处选择

# 使用两个矩阵，一个矩阵存放路段类，另一个矩阵存放通路。
# 其中，每1个列表最多包含1000个点。为了性能考虑。
# 因此，矩阵的最大值边长也为1000
def mat_create(point_max, mat, start, end):
    # 假设最多100个点，这里是可以调整的
    n = random.randint(1, point_max)
    for i in range(0, n):
        for j in range(0, n):
            # 矩阵元素存放一个路段类
            # mat[i][j] = [random.randint(start, end), random.randint(start, end)]

            mat[i][j] = road(start,end)
    return mat


class Graph:
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("参数错误")
        self._mat = [mat[i][:] for i in range(vnum)]  # 做拷贝
        self._unconn = unconn
        self._vnum = vnum

    # 顶点个数
    def vertex_num(self):
        return self._vnum

    # 顶点是否无效
    # 该函数不会被使用（应该）
    def _invalid(self, v):
        return v < 0 or v >= self._vnum

    # 添加边
    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")
        self._mat[vi][vj] = val

    # 获取边的值
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")
        return self._mat[vi][vj]

    # 获得一个顶点的各条出边
    def out_edges(self, vi):
        if self._invalid(vi):
            raise ValueError(str(vi) + "不是有效的顶点")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edegs = []
        for i in range(len(row)):
            if row[i] != unconn:
                edegs.append((i, row[i]))
        return edegs

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" + "\nUnconnected: " + str(self._unconn)


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        super().__init__(mat, unconn)
        # vnum为顶点数
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("参数错误")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    # 添加顶点
    # 返回该顶点编号
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    # 添加边
    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise ValueError("不能向空图添加边")
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")

        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)  # 如果原来有到vj的边，修改mat[vi][vj]的值
                return
            if row[i][0] > vj:  # 原来没有到vj的边，退出循环后加入边
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    # 获取边的值
    # 这应该固定为1
    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + " or " + str(vj) + "不是有效的顶点")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    # 获得一个顶点的各条出边
    def out_edges(self, vi):
        if self._invalid(vi):
            raise ValueError(str(vi) + "不是有效的顶点")
        return self._mat[vi]
