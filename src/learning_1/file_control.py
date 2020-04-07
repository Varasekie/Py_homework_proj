fo = open('En_test.txt')

####先创造两个列表来存储A和B两组数据
speak_A = []
speak_B = []
count = 0

####打开文件
for eachline in fo:
    if eachline[:3] != '===':
        [role, saying] = eachline.split(':', 1)
        if (role == 'A'):
            speak_A.append(saying)
        if (role == 'B'):
            speak_B.append(saying)
    else:
        ####注意这里是str（count），如果为‘count’就只是添加字符串
        file_nameA = 'A' + str(count) + '.txt'
        file_nameB = 'B' + str(count) + '.txt'

        f1 = open(file_nameA, 'w')
        f2 = open(file_nameB, 'w')
        f1.writelines(speak_A)
        f2.writelines(speak_B)

        speak_B = []
        speak_A = []
        count = count + 1

        f1.close()
        f2.close()


fo.close()
