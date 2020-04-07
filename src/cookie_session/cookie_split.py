
def cookie_split():
    f = open('cookie.txt','r')

    cookie = {}
    #将f中的内容，按分号隔开
    for line in f.read().split(';'):
        #将name和value键值对分开来
        name, value = line.strip().split('=', 1)

    #进行测试，看name和value是否已经分开了
    print(name)
    print(value)

    cookie[name] = value

    return cookie




