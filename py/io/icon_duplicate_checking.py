import re
from py.utils import IO_util


def get_icon_from_file_path(paths):
    temp = set()
    for path in paths:
        for file in IO_util.get_all_file(path):
            temp |= get_icon_from_file(file)
    return temp


def get_icon_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(re.findall(iconExg, f.read()))


findPath = [r'E:\SHT\project\sas-web\src\main\webapp\src\default\js',
            r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\default']
iconPath = r'E:\SHT\project\sas-web\src\main\webapp\res\default\fonts\iconfont.css'
iconExg = re.compile(r'(?m)icon-\w+')
iconList = get_icon_from_file_path(findPath)
filesIconList = get_icon_from_file(iconPath)
print('iconList')
print(iconList)
print('fileIcon')
print(filesIconList)

print(iconList - filesIconList)

print(filesIconList - iconList)



