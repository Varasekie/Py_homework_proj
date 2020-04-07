class A_relative:
    def unsure(self):
        print("输入插值")
        numerators = input()
        print("输入参数")
        denominator = input()

        print(str(self) + "相对不确定度A为")
        print(float(numerators) / float(denominator))

        return float(numerators) / float(denominator)


if __name__ == '__main__':
    total = 0
    # for  i in range(1,1200000):
    #     if (1200000%i == 0):
    #         total = total + 1
    #
    # print(total)95
#
# for i in range(1, 2019):
#     if (str(9) in str(i)):
#         total = total + 1
#
# print(total)

length = A_relative()
len = length.unsure()

#
# bridge= A_relative()
# bridge.unsure()
#
# height = A_relative()
# height.unsure()
