# 读取两个文件
# 使用utf-8格式打开文件
f1 = open("file1.txt", 'r', encoding="UTF-8")
f2 = open("file2.txt", 'r')
# 通过readlines，读出文件，以列表形式存储
lines1 = f1.readlines()
lines2 = f2.readlines()
# merge打开
with open("merge.py", 'w+') as f:
    if (lines1 is not None) & (lines2 is not None):
        # 用n记录哪个是较短的一个
        n = min(len(lines1), len(lines2))
        # 交替写入文件
        for i in range(0, n - 1):
            f.write(lines1[i])
            f.write(lines2[i])
        # 第一个文件较小，就直接写入剩下的全部文件，反之写第一个
        if n == len(lines1):
            for i in range(n, len(lines2)):
                f.write(lines2[i])
        else:
            for i in range(n, len(lines1)):
                f.write(lines1[i])
        # 移动指针到第一个，然后开始读取文件
        f.seek(0)
        lists = f.readlines()
        for i in lists:
            print(i)
