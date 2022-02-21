import re


def judge(password):
    # 初始密码等级为0
    level = 0
    # 保证密码为字符串，方便利用正则表达式筛选
    password = str(password)
    # search返回第一个匹配的，如果没有匹配的就返回None
    # 分别匹配数字，小写字母，大写字母，长度
    if re.search(r'[0-9]', password) is not None:
        level = level + 1
    if re.search(r'[a-z]', password) is not None:
        level = level + 1
    if re.search(r'[A-Z]', password) is not None:
        level = level + 1
    if len(password) >= 8:
        level = level + 1
    # 由于最后需要输出，所以需要设定一个返回值
    return level


while True:
    s = input("请输入测试密码，回车退出")
    if s == "\r":
        break
    print(judge(s))
