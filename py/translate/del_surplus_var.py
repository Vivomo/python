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
        read_content = f.read()
        lang_name_match = re.search(langNameExp, read_content)
        lang_name = 'global'
        if lang_name_match:
            lang_name = lang_name_match.groups()[0]
        var_set = set([e.groups()[0] for e in re.finditer(var_ftl_reg, read_content)])
    return lang_name, var_set


def get_lang_dict():
    temp_dict = {}
    for p in IO_util.get_all_file(enPath):
        key, value = get_language_var(p)
        temp_dict[key] = value
    return temp_dict


def filter_var(file_path):

    global globalSetCopy
    global langDict

    lang_name, ftl_var_set = get_language_var_ftl(file_path)
    globalSetCopy -= ftl_var_set
    langDict[lang_name] -= ftl_var_set - globalSet


def del_file_var(file_name, var_set, find_global=False):
    del_lines = []
    with open(os.path.join(enPath, 'l_%s.ftl' % file_name), 'r', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            result = re.search(var_reg, line)
            if result and result.group() in var_set:
                if find_global:
                    pass
                else:
                    del_lines.append(i+1)


def is_same_global_var(line):
    pass


var_reg = re.compile('l_\w+')
var_ftl_reg = re.compile(r'(?m)\$\{\s*(l_\w+)\s*\}')


testPath = r'E:\git\pythonCode\test\translate\read\event_order.ftl'
testPath2 = r'E:\git\pythonCode\test\translate\write\en\l_event_order.ftl'

pc1Path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\default'
pc2Path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\saishi'
wapPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\waptemplate\default'
enPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'

pathArr = (pc1Path, pc2Path, wapPath)

langNameExp = r'lang_name\s?=\s?[\'\"](\w+)[\'\"]'
# print(get_language_var_ftl(testPath))
# print(get_language_var(testPath2))

langDict = get_lang_dict()
globalSet = langDict['global']
globalSetCopy = copy.copy(globalSet)

for path in pathArr:
    for file in IO_util.get_all_file(path):
        filter_var(file)

print(globalSetCopy)
for k, v in langDict.items():
    if v and k != 'global':
        print(k, '-->', v)
        print('待定:', v & globalSet)
        print('需要删除', v - globalSet)


# print(get_language_var_ftl(testPath))


