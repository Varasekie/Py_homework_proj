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

def getlist(str):
    list_net = []
    regax1 = r'.+\.jpg'
    regax = r'href="http.+?"'
    matchObj = re.findall(regax,str)
    # print(matchObj)

    regax2 = r'http.+?html'
    pattern2 = re.compile(regax2)

    for i in matchObj:
        net = re.search(pattern2, i)
        if net:
            list_net.append(net.group())

    print(list_net)



if __name__=='__main__':
    str = get_url_message()
    getlist(str)
