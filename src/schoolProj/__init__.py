import xml
# coding=utf-8
import xml.dom.minidom

# print("1")

# 打开xml文档
dom = xml.dom.minidom.parse('D:\\learning\\map\\test.osm')

# 得到文档元素对象
print("2")

root = dom.documentElement
# 15行不确定，运行bug的话就删
# nodes = dom.getElementsByTagName('node')
print("3")

print(root.nodeName)
print("4")
