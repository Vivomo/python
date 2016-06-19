import re
import os
import http.client
import hashlib
import urllib.parse
import random
import json

# readPath = r'E:\git\pythonCode\test\translate\read'
readPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\default'
# writePathZh = r'E:\git\pythonCode\test\translate\write\zh'
# writePathEn = r'E:\git\pythonCode\test\translate\write\en'
writePathZh = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\zh'
writePathEn = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
chineseReg = u"[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+"

appid = '20160607000022958'
secretKey = 'lCxFBKsQHEvNw7RRFapW'


def get_all_file(file_path):
    file_list = []

    for p, d, f in os.walk(file_path):
        for f1 in f:
            file_list.append(os.path.join(p, f1))
    return file_list


def format_assign(zh):
    _r = int(random.random() * 100000000)
    return {
        'zh': '\tl_%d = "%s" <#--%d-->\n' % (_r, zh, _r),
        'en': '\tl_%d = "word_blank" <#--%d--> <#--%s-->\n' % (_r, _r, zh),
        'chinese': zh
    }


def translate_word(words, from_lang='zh', to_lang='en', times=0):
    http_client = None
    salt = int(random.random()*10000000)
    sign = bytes(appid + words + str(salt) + secretKey, encoding='utf-8')
    m1 = hashlib.md5()
    m1.update(sign)
    sign = m1.hexdigest()
    url = '/api/trans/vip/translate'
    url = url + '?appid=' + appid + '&q=' + urllib.parse.quote(
        words) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
        http_client.request('GET', url)
        resp = http_client.getresponse().read()
        translate_result = json.loads(resp.decode('utf-8')).get('trans_result')
        if not translate_result:
            print(json.loads(resp.decode('utf-8')).get('error_code'))
            if times < 3:
                translate_word(words, times=times+1)
            else:
                print('Error 3 times')

        return translate_result
    except Exception as e:
        print(e)
    finally:
        if http_client:
            http_client.close()


def format_translate(format_words, translate_result, file_name):
    """
    translate_result [{'dst': '苹果', 'src': 'apple'}, {'dst': '橙色', 'src': 'orange'}]
    """
    if not translate_result:
        print('Translate Error for' + file_name)
        return
    for i, dict_w in enumerate(format_words):
        try:
            dict_w['en'] = dict_w['en'].replace('word_blank', translate_result[i]['dst'])
        except Exception as e:
            print(e)
            print('Error for ' + file_name)


def fetch_chinese(file_list):

    for path in file_list:
        with open(path, 'r', encoding='utf-8') as r_file:
            file_name = os.path.basename(r_file.name)
            write_file_path_zh = os.path.join(writePathZh, file_name)
            write_file_path_en = os.path.join(writePathEn, file_name)
            with open(write_file_path_zh, 'w', encoding='utf-8') as w_file_zh:
                w_content_zh = ['<#assign\n']
                temp_content = set()
                for line in r_file.readlines():
                    zh_arr = re.findall(chineseReg, line)
                    for zh in zh_arr:
                        temp_content.add(zh)

                zh_list = list(temp_content)
                format_words = list(map(format_assign, zh_list))
                format_translate(format_words, translate_word('\n'.join(zh_list)), file_name)
                zh_content = list(map(lambda w_json: w_json.get('zh'), format_words))
                w_content_zh += zh_content
                w_content_zh.append('>')
                w_file_zh.write(''.join(w_content_zh))

            with open(write_file_path_en, 'w', encoding='utf-8') as w_file_en:
                w_content_en = ['<#assign\n']
                en_content = list(map(lambda w_json: w_json.get('en'), format_words))
                w_content_en += en_content
                w_content_en.append('>')
                w_file_en.write(''.join(w_content_en))


# fileList = get_all_file(readPath)
# fetch_chinese(fileList)




