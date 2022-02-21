# 打开新文件
with open('merge_new.py', 'w+') as f:
    # 打开旧文件
    f1 = open("merge.py", 'r')
    # 以列表形式读旧文件
    lines = f1.readlines()
    # 由于需要去掉\n，所以需要将最大长度-1
    maxLine = len(max(lines, key=len)) - 1
    # 写入文件，写入字符串去掉\n，加最大值-现有值的空格数量，+＃+行号，最后需要补上\n
    for i in range(0, len(lines)):
        strs = str(lines[i])[:-1] + ' ' * (maxLine - len(lines[i][:-1]) + 1) + "#" + str(i) + "\n"
        f.write(strs)
    # 移动文件的指针到文件头，否则无法读出
    f.seek(0)
    line = f.read()
    print(line)
    f1.close()
