import requests
url = 'https://mooc1-2.chaoxing.com/mycourse/studentcourse?courseId=209185064&clazzid=18563006&vc=1&cpi=106370187&enc=cba80d78eb4605ded056492337b5dc7d'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'Host': 'mooc1-2.chaoxing.com',
    # 'Referer': 'http://mooc1-2.chaoxing.com/visit/interaction?s=b6571ca640a34b65c480356261c170c4',
    'Cookie':'uname=202190301; lv=1; fid=2815; _uid=116148942; uf=da0883eb5260151e64ab61a6e094655a6a13334312a3545a70b16adae36141111e84613d6491a61b10cc7e014c79b730913b662843f1f4ad6d92e371d7fdf64412a93b9892076202102289339c6dea121471850d8bf7e34cbcc99e73b1038a33f9ef6e84a4c10c87; _d=1596089998364; UID=116148942; vc=CB3F01115F66427999838934CD5C23D9; vc2=E610658F7D8D98370D5E31FE6D69EE1D; vc3=IHbNmX9c4KhB8luK9rXVU44sID1Swvve%2FMZn%2FbaKiRp17NZ0d8EBtHzQENVhqYpE7DWrcoL9IJTCtY3%2BLSVP0tzAPQYRu8u%2FCsvpOOorxfaBBpwGvvh%2Be6llXZAHbIkdQlK8k00E3X90HT2Tk7%2Bl82r2frY66g1p9fi2JZU3D1A%3Db4c280edb8ed3b8ecd06760e20627a6e; xxtenc=818c3c3c90dc496c713ad4121c499cfe; DSSTASH_LOG=C_38-UN_1642-US_116148942-T_1596089998365; tl=1; k8s=ad4fd3b308a25ba4cd45b00b3926660aa6d34b1f; jrose=8397EE12DC7D165D1620833EA0612EBE.mooc-1110545951-8dh90; route=ac9a7739314fa6817cbac7e56032374b; thirdRegist=0; source=""'
}


def get_connection(url):
    response = requests.get(url, headers=headers)
    print(response.content.decode('utf-8'))
    return response.content.decode('utf-8')

import re


# 所有网页的网址
def get_object_Id(str):
    # 第一次正则提取
    regax = r'<a href=\'/mycourse/studentstudy.+?\''
    # regax1 = r'<a href="/mycourse/studentstudy.+?"'
    pattern1 = re.compile(regax)
    matchObj1 = re.findall(pattern1, str)
    print(matchObj1)

    # 第二次正则
    matchObj = []
    regax2 = r'\'.+?\''
    pattern2 = re.compile(regax2)
    for obj in matchObj1:
        matchObj2 = re.findall(pattern2, obj)
        # print(matchObj)
        matchObj.append(matchObj2[0])
    print(matchObj)

# 去掉双引号
    list_web = []
    for objs in matchObj:
        match = objs.split("'", 2)[1]
        list_web.append(match)
    print(list_web)
    # 最终的网站列表
    for i in  range(0,len(list_web)):
        temp = 'http://mooc1-1.chaoxing.com'+list_web[i]
        list_web[i] = temp
    print(list_web)
    return list_web
    # print(len(list_web))

# 根据网页的列表，筛选objectid
def search_object_id():
    pass
# 保存文件
def save_pdf():
    pass
# get_connection()
str = get_connection(url = 'https://mooc1-2.chaoxing.com/mycourse/studentcourse?courseId=209185064&clazzid=18563006&vc=1&cpi=106370187&enc=cba80d78eb4605ded056492337b5dc7d')
list_web = get_object_Id(str)

# 访问列表的网站，得到obecjtid
s = get_connection(url =list_web[0])

# print(s)