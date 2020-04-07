import requests
import importlib
split = importlib.import_module('cookie_split')

#写好url和header，形成反反爬机制
url = 'http://www.douban.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
           'Referer':'https://www.douban.com/',
           'Host':'www.douban.com'
           }

####调用函数，但是仍然需要人工先登录拿到cookies，要先复制到该txt中，才能拿得到
####这一步将拿到的cookie数值转化为字典的形式
cookies = split.cookie_split()
print('cookie的值为')
print(cookies)

#带着cookies去拿response
response = requests.get(url,headers = headers ,cookies = cookies)

#打印结果
print('situation：')
print(response.status_code)
#print('请求结果')
#print(response.text)

####接下来是session
#此处url没有变化，直接沿用上面的
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
           'Referer':'https://www.douban.com/',
           'Host':'www.douban.com'
           }
session1 = requests.session()

formdata = {
    ''
}





