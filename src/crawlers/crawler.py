import requests
import re

def get_url_message():
    url = 'https://tieba.baidu.com/p/2125372029#!/l/p1'
    Header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Host': 'tieba.baidu.com'
        # 还有一个没找到的referer
        }
    response = requests.get(url, Header)
    # print(response.status_code)
    str = response.text
    return str


def find_url(string):
    list = []
    regax1 = r'src=".+?.jpg"'
    matchObj1 = re.findall(regax1,string)
    # print(matchObj1)
    regax2 = r'https://imgsa.+?\.jpg'
    pattern = re.compile(regax2)

    for i in matchObj1:
        x = pattern.search(i)
        if x :
            a = x.group()
            list.append(a)

    print(list)

    return list

def save_picture(list):
    Header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Host': 'tieba.baidu.com'
        # 还有一个没找到的referer
    }
    for i in list:
        response = requests.get(i,Header)
        file_name = i.split('/')
        # print(file_name[-1])
        f = open('pics/'+file_name[-1],'wb')
        f.write(response.content)
        f.close()
        print(i+'下载成功')
    print('下载结束')


if __name__ == '__main__':
    str = get_url_message()
    list = find_url(str)
    # save_picture(list)
