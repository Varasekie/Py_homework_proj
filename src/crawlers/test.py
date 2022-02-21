import requests
from fake_useragent import UserAgent
from lxml import etree
ua = UserAgent()
print(ua.chrome)
url = "https://movie.douban.com/subject/26266893/reviews?start=120"
headers = {'User-Agent': ua.chrome}
r = requests.get(url,headers)
print(r)
