class bicycle:
    # 只需要定义一个函数，表明用自行车走了多久即可。
    # 在这里，km不需要作为对象属性进行运算。
    # 如有必要也可以作为对象属性
    def run(self, km):
        print("自行车骑行距离", km)


# 继承类，继承bicycle
class Ebicycle(bicycle):
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, vol):
        print('充电', vol, '升')
        self.valume = self.valume + vol

    # km是要骑行的里程，每骑行10km消耗电量1度。
    def run(self, km):
            # 当电量允许，输出电动自行车骑行的里程
        if self.valume * 10 > km:
            # 要减去油量
            self.valume = self.valume - km / 10
            print("电动车骑行的里程为", km)
        else:
            # 当电量消耗尽时，调用Bicycle的run方法骑行
            print("电动车骑行的里程为", self.valume * 10)
            # 输出余下的用自行车骑行的里程。
            bicycle.run(self, km - self.valume * 10)
            self.valume = 0


b = Ebicycle(5)  # 一个电池余量为5度的电动行车
b.run(10)  # 骑行10km
b.run(100)  # 骑行100km
b.fill_charge(6)  # 充了6度电，
b.run(70)  # 骑行70km
