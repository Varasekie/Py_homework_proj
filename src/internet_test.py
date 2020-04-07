from pip._vendor import requests

param = {'name': '左手指月'}
response = requests.get('https://api.apiopen.top/searchMusic', params=param)
print('http 响应状态是：')
print(response.status_code)
print('API调用结果：')
print(response.json())
print('API调用结果的数据类型：')
print(type(response.json()))
print('API调用结果的 message 值：')
print(response.json()['message'])
print('API调用结果的 第三首歌的标题：' + str(response.json()['result'][2]['title']))
print('API调用结果的 第三首歌的演唱者：' + str(response.json()['result'][2]['author']))