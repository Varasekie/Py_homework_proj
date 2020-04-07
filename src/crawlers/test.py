# import re
# import requests
#
#
# response = '<a class="ag_ele_a ag_ele_a_v" href="/photo/p?kw=%E6%A8%B1%E8%8A%B1%E5%BA%84%E7%9A%84%E5%AE%A0%E7%89%A9%E5%A5%B3%E5%AD%A9&amp;tid=2125372029&amp;pic_id=dc9095d4b31c87013860ed3d267f9e2f0508ff7f" target="_blank" style="height:337px;" onclick="AlbumStatistic.send(3012);"><img src="https://imgsa.baidu.com/forum/w%3D223/sign=18205330b7fd5266a72b3b16981a9799/dc9095d4b31c87013860ed3d267f9e2f0508ff7f.jpg" style="width:223px;height:337px;left:0px;top:0px;"></a><img src="https://imgsa.baidu.com/forum/w%3D223/sign=18205330b7fd5266a72b3b16981a9799/dc9095d4b31c87013860ed3d267f9e2f0508ff7f.jpg" style="width:223px;height:337px;left:0px;top:0px;"><a class="ag_ele_a ag_ele_a_v" href="/photo/p?kw=%E6%A8%B1%E8%8A%B1%E5%BA%84%E7%9A%84%E5%AE%A0%E7%89%A9%E5%A5%B3%E5%AD%A9&amp;tid=2125372029&amp;pic_id=dc9095d4b31c87013860ed3d267f9e2f0508ff7f" target="_blank" style="height:337px;" onclick="AlbumStatistic.send(3012);"><img src="https://imgsa.baidu.com/forum/w%3D223/sign=18205330b7fd5266a72b3b16981a9799/dc9095d4b31c87013860ed3d267f9e2f0508ff7f.jpg" style="width:223px;height:337px;left:0px;top:0px;"></a>'
#
# regax = r'<img src="([^"].+?.jpg)'
# pattern = re.compile(regax)
# matchObj = re.findall(pattern,response)
# matchObj.append(matchObj)
# print(matchObj)


# regax1 = r'src="(http.+?.jpg)"'
# pattern1 = re.compile(regax1)
#
# matchObj1 = re.findall(pattern1, matchObj)
# # print(matchObj1)
#
# matchObj1.append(matchObj1)
#
# print(matchObj1)
#
# a = pow(2/15,2)
# b = pow(2/12.76,2)
# c = pow(1/82.85,2)
#
# d = pow(a+b+c,0.5)
# print(d*0.02)
# print(d*4043.78*0.02)
#
# a = pow(0.005,2)
# b = pow(0.01,2)
# c = (a+b)*2/5/6
# d = 0.004*0.004/3
#
# print(pow(c+d,0.5))
#
# a = pow(0.002,2)
# u = pow(d + a , 0.5)
#
# print(0.004/0.17)

a = pow(30 / (pow(15, 2) - pow(12.76, 2)), 2) * pow(0.013, 2)
b = pow(2 * 12.76 / (pow(15, 2) - pow(12.76, 2)), 2) * pow(0.013, 2)
c = pow(0.015 / 82.07, 2)
d = pow(a+b+c,0.5)
e = 4008.13*d
print(d)
print(e)
