import http.client
import hashlib
import urllib.parse
import random
import json

m1 = hashlib.md5()
appid = '20160607000022958'
secretKey = 'lCxFBKsQHEvNw7RRFapW'


q = 'orange\napple'


def translate_world(words, from_lang='zh', to_lang='en'):
    http_client = None
    salt = random.randint(32768, 65536)
    sign = bytes(appid + q + str(salt) + secretKey, encoding='utf-8')
    m1.update(sign)
    sign = m1.hexdigest()
    url = '/api/trans/vip/translate'
    url = url + '?appid=' + appid + '&q=' + urllib.parse.quote(
        words) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
        http_client.request('GET', url)
        resp = http_client.getresponse().read()

        return json.loads(resp.decode('utf-8')).get('trans_result')
    except Exception as e:
        print(e)
    finally:
        if http_client:
            http_client.close()
