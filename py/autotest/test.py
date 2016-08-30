import json
import re
from bs4 import BeautifulSoup

from py.autotest import  html_parser, html_downloader
# with open('data.json', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(json.loads(content))

downloader = html_downloader.HtmlDownloader()
content = downloader.download('http://vimo.360jlb.cn', 'html.parser', from_encoding='utf-8')
soup = BeautifulSoup(content)
# print(soup.get_text())
print('/////////////////////////////////////////////////////////////////////////////////')
print(soup.getText())


