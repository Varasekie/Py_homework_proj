
import requests
import importlib
fib = importlib.import_module('utils')

#### cookie
url = 'https://www.douban.com/mine'
header = {'Referer':'https://www.douban.com', 'Host':'www.douban.com', 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
cookies = fib.readCookie()
print(cookies)
response = requests.get(url, headers=header, cookies=cookies)
print('http 响应状态是：')
print(response.status_code)
print('页面请求结果：')
print(response.text)