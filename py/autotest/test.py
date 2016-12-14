import json
import re
from urllib import request, parse
from bs4 import BeautifulSoup

from py.autotest import  html_parser, html_downloader


# with open('data.json', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(json.loads(content))

with open('data.json', 'r', encoding='utf-8') as jsonFile:
    data = json.loads(jsonFile.read())
postData = parse.urlencode(data).encode()
resp = request.urlopen('http://www.360paobu.com/rest/user/login', data=postData)

print(type(resp.headers))



