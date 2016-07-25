import http.cookiejar
import urllib
from urllib import parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def url_open(url):
    req = Request(url)
    # connect.sid=s%3AnUAoKRYkjbuHOu_iqidLhVyhE99dFz6e.5aA4tjO4Z9vr0JM3HWI7r2PXeScXd1CYaHzDKZyHb%2BA; SERVERID=9c84a525c675ef4651cf84dcd65978c2|1467710737|1467710720 --JSESSIONID=BBD8721C2AE6F65AA45B102B9BF7E978;
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    req.add_header('Cookie', '_AC_ID_=Rmxaq%2BmnZBXd6TlyvT6waUXHvJVy9R6x; _AC_CRT_DAT_=1467710720944; _AC_SIG_=aa60a42ceabd9c9b45ecace68b086b3c; ')
    data = {"page":1,"pageSize":100,"orderType":-1,"sortId":"0","state":"-1","title":""}

    postdata = parse.urlencode(data)

    response = urlopen(req, data=postdata.encode())
    return response.read().decode('utf-8')

url = 'http://lysh.lv-guanjia.com/api/activity/activity-list/'
print(url_open(url))


