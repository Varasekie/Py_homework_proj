import requests
import re
import csv as csv

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.116 Safari/537.36'}
# 要访问的
url = 'http://college.gaokao.com/schlist/'
# 初始化列表,page可以规定要爬取的页数
# 初始化四个列表，是我想要爬取的四个数据列，学校名称，学校网站，学校地址，学校所属
page = 5
list_location = []
list_feature = []
list_web = []
list_name = []


# 定义数据处理的函数，为了能返回一个列表。
def deal(regax, text, start, end, list):
    match = re.findall(regax, text)
    for i in range(0, len(match)):
        match[i] = match[i][start:end]
    list.extend(match)
    return


# for循环，循环页面爬取
for i in range(1, page + 1):
    url = " http://college.gaokao.com/schlist/p" + str(i)

    texts = requests.get(url, Headers, timeout=10).text
    # 1.处理名字
    regex_name = r'<strong title=".+?"blue'
    regex_name = re.compile(regex_name)
    # 对数据进行筛选
    deal(regex_name, texts, 15, -13, list_name)
    # 2.处理地理位置
    regex_location = r'<li>高校所在地.+?</li>'
    regex_location = re.compile(regex_location)
    deal(regex_location, texts, 10, -5, list_location)
    # 3.处理网站
    regex_web = r'<li>学校网址.+?</li>'
    regex_web = re.compile(regex_web)
    deal(regex_web, texts, 9, -5, list_web)
    # 4.处理特征
    regex_feature = r'<li>高校隶属.+?</li>'
    regex_feature = re.compile(regex_feature)
    deal(regex_feature, texts, 9, -5, list_feature)

# 写入csv文件
f = open('schools.csv', 'w', encoding="UTF-8")
list_row = []
for i in range(0, len(list_web)):
    if list_name[i] is not None:
        list = [list_name[i], list_location[i], list_web[i], list_feature[i]]
        list_row.append(list)
write = csv.writer(f)
write.writerows(list_row)
