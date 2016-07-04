import re
import copy
from py.utils import IO_util


def del_dict_key(_dict, key):
    if key in _dict:
        del _dict[key]

# reg = re.compile(r'l_\w+')
# var_reg_ftl = re.compile(r'\$\{\s*(\w+)\s*\}')
# print(re.search(var_reg_ftl, '${ l_aaa}').groups()[0])

g = {1, 2, 3, 4, 5}
a = {4, 5, 6}
# print(a - g)

langNameExp = r'lang_name\s?=\s?[\'\"](\w+)[\'\"]'
s = "<#global lang_name = 'user'>"
r = re.search(langNameExp,s)
# print(r)
# print(r.groups()[0])
testPath = r'E:\git\pythonCode\test\translate\write\chinese_js.txt'
# IO_util.del_file_lines(testPath, [1, 3, 5, 8, 9])

with open(testPath, 'r+', encoding='utf-8') as f:
    lines = f.readlines()
    f.write(''.join(lines[1:10]))
    print(lines)
