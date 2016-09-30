import http.cookiejar
import urllib
from urllib import parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def url_open(url, data):
    req = Request(url)
    # connect.sid=s%3AnUAoKRYkjbuHOu_iqidLhVyhE99dFz6e.5aA4tjO4Z9vr0JM3HWI7r2PXeScXd1CYaHzDKZyHb%2BA; SERVERID=9c84a525c675ef4651cf84dcd65978c2|1467710737|1467710720 --JSESSIONID=BBD8721C2AE6F65AA45B102B9BF7E978;
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    req.add_header('Cookie', 'JSESSIONID=4DC80577CF62B19A6CB0DE38A0DBA681-n1')

    postdata = parse.urlencode(data)

    response = urlopen(req, data=postdata.encode())
    return response.read().decode('gbk')


u = 'http://221.226.28.67:88/jsswxxSSI/water_selectWaterAndStStbprpBAndWaterWarJson.action'
u2 = 'http://221.226.28.67:88/jsswxxSSI/water_selectWaterDataJson.action'
# print(url_open(u, {"ajaxVal": 2,
#                    "waterType": "1-2-3-4-5",
#                    "startTime": "2016-09-24 08:00:00",
#                    "endTime": "2016-09-26 11:18:31",
#                    "type": 0,
#                    "id": 0,
#                    "timestamp": 14748599123,
#                    "tId": '',
#                    "isTopic": ''}))
print(url_open(u2, {
    "startTime": "2016-09-25 11:15:00",
    "stcd": "51107800",
    "endTime": "2016-09-29 11:15:00",
    "sttp": "RR"
}))
