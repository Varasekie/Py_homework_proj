# 对Test2/T4的改进，将多个用户密码放在一个字典中
usr_pass = {'admin':'abc','test':'test','cly':'cly'}
print("===========欢迎使用ATM机==========")
# opp变量控制循环次数不大于3次
opp = 0
# 通过条件判断，是否登录成功
while opp < 3:
    print("请输入用户名和密码")
    username = input("用户名：")
    password = input("密码：")
    # 如果不在集合中
    if username not in usr_pass.keys():
        print("用户名错误，用户不存在")
        print("你还有" + str(3 - opp - 1) + '次机会')
        opp = opp + 1
        continue
    # 判断是否一一对应,字典的按索引访问
    if password != usr_pass[username]:
        print("用户名正确密码错误---登录失败")
    else:
        print("用户名正确密码正确---登录成功")
        break
    # str（）格式转换
    print("你还有" + str(3 - opp-1) + '次机会')
    opp = opp+1
if opp == 3:
    print("==========超过三次登录失败，吞卡============")