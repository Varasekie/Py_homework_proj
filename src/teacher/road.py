class road:
    a = 0.5

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.l = pow(pow(start, 2) + pow(end, 2), 0.5)


    def test_location(self, location):
        # 此处只是做最简单的直线判断。（这个判断有可能是并不必要的。当道路虽然是弯曲的。此处只是作近似
        # 可能需要一个误差估计……误差估计应该可以通过曲率来计算）
        # location是一个列表，x为x轴数据，y为y轴数据
        # location = list(location)
        k = abs((self.end[1] - self.start[0]) / self.end[0] - self.start[0])
        # b = y-kx
        b = self.end[1] - k * self.start[0]
        if (abs(location[1] - k * location[0] - b) < self.a):
            return True
        else:
            return False
