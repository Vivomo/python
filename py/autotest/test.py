import json
import re
from urllib import request, parse
from bs4 import BeautifulSoup

from py.autotest import  html_parser, html_downloader


# with open('data.json', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(json.loads(content))

data = {
    'username' : 'wbtest1@163.com',
    'password' : '123456'
}
postData = parse.urlencode(data).encode()
resp = request.urlopen('http://www.360paobu.com/rest/user/login', data=postData)

print(type(resp.headers))



