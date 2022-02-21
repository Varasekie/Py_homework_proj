import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# path规定读取csv的路径
path = "student.csv"
# 使用pandas读csv，content自动返回DataFrame类型
content = pd.read_csv(path, encoding="gbk")
n = len(content['math'])
sum_score_list = []
# 使用for循环，将其列的每一项相加，得到math和python成绩的和
for i in range(0, n):
    sum_score_list.append(content['math'][i] + content['python'][i])
# DataFrame可以直接通过赋值添加列。
content['sum_score'] = sum_score_list
# 写会文件
content.to_csv('student2.csv',sep=',')
content = pd.read_csv(path, encoding="gbk")
# 画图部分，横轴为号码，纵轴为成绩
plt.plot(content["no"], content["python"])
plt.plot(content["no"], content["math"])
# 添加图例
matplotlib.rcParams['font.family'] = 'FangSong'
plt.legend(["python", "math"])
plt.title('students score' )
plt.xlabel('number')
plt.ylabel('score')
plt.show()
