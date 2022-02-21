fst_busstop=["龙江","阳光广场","汉江路","嫩江路","清凉山公园","拉萨路","五台山","莫愁路"]
first = input("请输入起点站")
last = input("请输入终点站")

# 字符匹配
f1 = fst_busstop.index(first)
l1 = fst_busstop.index(last)

if(l1<f1):
    print("您需要乘坐反方向线路")
else:
    e = l1-f1+1
    print("从"+str(first)+'到'+str(last) +'需要' +str(e) +'站路')