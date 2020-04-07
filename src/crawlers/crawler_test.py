import os
import requests
import re


def getDef():
    url = 'https://tieba.baidu.com/p/2125372029'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Host': 'tieba.baidu.com',
        'Referer': 'https://tieba.baidu.com/p/2125372029'
    }

    response = requests.get(url, headers=headers)
    return response.content.decode('utf-8')
    # print(response.content.decode('utf-8'))


def findImg(response):
    ####用正则表达式进行筛选
    regax1 = r'<img src="[^"].+?"'
    pattern1 = re.compile(regax1)

    matchObj1 = re.findall(pattern1, response)
    print(matchObj1)

    matchObj1.append(matchObj1)

    print(matchObj1)

    return matchObj1


def downloadFile(img_add):
    for each in img_add:
        filename = each.split("/")[-1]
        print(filename)
        for each in img_add:
            with open(filename, mode='ab') as f:
                img = requests.get(each).content
                f.write(img)


def crawler_test(file='test1'):
    os.mkdir(file)
    ####改变根目录
    os.chdir(file)

    ####请求
    responses = getDef()
    # print(responses)

    ####筛选
    add = findImg(responses)

    ####下载

    downloadFile(add)

if __name__ == '__main__':
    file = 'test1'
    crawler_test(file)
    print('over')
