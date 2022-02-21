import requests
import re

def get_url_message():
    url = 'https://book.douban.com/tag/%E6%95%A3%E6%96%87'
    Header = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'User-Agent': 'ua.chrome',
        # 'Host': 'tieba.baidu.com'
        # 还有一个没找到的referer
        }
    response = requests.get(url,Header)
    print(response.status_code)
    str = response.text
    print(str)
    return str

def getlist(str):
    list_net = []
    regax_pic = r'https://img2.doubanio.com/view/subject/s/public/'
    regax = r'href="http.+?"'
    matchObj = re.findall(regax_pic,str)
    print(matchObj)

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
