import re
import copy


def del_dict_key(_dict, key):
    if key in _dict:
        del _dict[key]

# reg = re.compile(r'l_\w+')
# var_reg_ftl = re.compile(r'\$\{\s*(\w+)\s*\}')
# print(re.search(var_reg_ftl, '${ l_aaa}').groups()[0])

g = {1, 2, 3, 4, 5}
a = {4, 5, 6}
print(a - g)

