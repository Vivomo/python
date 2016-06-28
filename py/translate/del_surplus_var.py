import os
import re
import copy
from py.utils import IO_util


def del_dict_key(_dict, key):
    if key in _dict:
        del _dict[key]


def get_language_var(file_path):
    var_set = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            result = re.search(var_reg, line)
            if result:
                var_set.add(result.group())
    return re.search(r'l_(\w+)', os.path.basename(file_path)).groups()[0], var_set


def get_language_var_ftl(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        var_set = set([e.groups()[0] for e in re.finditer(var_ftl_reg, f.read())])
    return re.search(r'(\w+)', os.path.basename(file_path)).group(), var_set


def get_lang_dict():
    en_path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
    temp_dict = {}
    for p in IO_util.get_all_file(en_path):
        key, value = get_language_var(p)
        temp_dict[key] = value
    return temp_dict


def filter_var(file_path):

    global globalSet
    global langDict

    basename, ftl_var_set = get_language_var_ftl(file_path)
    globalSet -= ftl_var_set
    langDict[basename] -= ftl_var_set - langDict['global']
    

var_reg = re.compile('l_\w+')
var_ftl_reg = re.compile(r'(?m)\$\{\s*(l_\w+)\s*\}')


testPath = r'E:\git\pythonCode\test\translate\read\event_order.ftl'
testPath2 = r'E:\git\pythonCode\test\translate\write\en\l_event_order.ftl'

pc1Path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\default'
pc2Path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\saishi'
wapPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\waptemplate\default'
pathArr = (pc1Path, pc2Path, wapPath)
# print(get_language_var_ftl(testPath))
print(get_language_var(testPath2))

langDict = get_lang_dict()
globalSet = copy.copy(langDict['global'])

for path in pathArr:
    for file in IO_util.get_all_file(path):
        filter_var(file)

print(globalSet)
print(langDict)





