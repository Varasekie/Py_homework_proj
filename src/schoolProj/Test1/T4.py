import random
flag = True
while flag:
    # 单词集
    WORDS = ["bookstore",'house','plant','rose']
    # 随机选择一个单词
    word = random.choice(WORDS)
    # 保留单词，之后需要对word进行改变
    word_normal = word
    # 乱序排列
    jumble = ''
    lens = len(word)
    for i in range(0,lens):
        k = random.choice(word) #随机选择字母
        jumble = jumble + k #保留乱序单词
        num = int(word.index(k))#获取下标
        word = word[0:num]+word[int(word.index(k))+1:len(word)]#字符串拼接
    print("乱序后的单词",'')
    print(jumble)
    print("您猜测的结果",'')
    s = input()
    while s != word_normal:
        print("请继续猜测")
        s = input()
    print("成功")
    print("是否继续y/n")
    # 如果不继续就跳出循环
    flag = False if input() == 'n' else True

