import re
import os

from py.translate import translate

pcJSPath = r'E:\SHT\project\sas-web\src\main\webapp\src\default\js'
wapJSPath = r'E:\SHT\project\sas-web\src\main\webapp\src\m\js'
pathArr = [pcJSPath, wapJSPath]
jsDict = {}
js_chinese_path = r'E:\git\pythonCode\test\translate\write\chinese_js.txt'


def fetch_chinese(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chinese_set = set(re.findall(translate.chineseReg, file.read()))
        key = os.path.basename(file_path)
        if key in jsDict:
            jsDict[key] = jsDict[key] | chinese_set
        else:
            jsDict[key] = chinese_set


for path in pathArr:
    for p in translate.get_all_file(path):
        fetch_chinese(p)

with open(js_chinese_path, 'w', encoding='utf-8') as cFile:
    for (k, value) in jsDict.items():

        print(k, end='\n', file=cFile)
        print(','.join(value), end='\n', file=cFile)
