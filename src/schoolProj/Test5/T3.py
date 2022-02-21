# 以可以读的方式打开文件
with open("如梦令.txt", 'r+', encoding="UTF-8") as f:
    # 读出文件
    lines = f.read()
    # 指针移动到文件头
    f.seek(0)
    # 写入词牌名和作者
    f.write("如梦令·昨夜雨疏风骤\n[宋] 李清照\n")
    # 再写入原本的内容
    f.write(lines)
    f.write("\n")
    # 写姓名
    f.write("陈零壹抄录")
    # 指针移动到文件头，准备读文件
    f.seek(0)
    line = f.read()
    print(line)