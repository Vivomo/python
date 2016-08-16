from py.utils import IO_util
import re

theme4Reg = re.compile(r'\$theme4:\s?(#\w+)')
skinReg = re.compile(r'\$slave:\s?(#\w+)')
skinFileReg = re.compile(r'skin\d+')


def get_theme_old():
    # 获取theme4
    file_path = r'E:\SHT\project\sas-web\src\main\webapp\src\default\scss'
    theme_color = []

    for path in IO_util.get_all_file(file_path):
        if path.find('theme') != -1:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    result = theme4Reg.search(line)
                    if result:
                        theme_color.append(result.groups()[0])
                        break
    return theme_color


def get_theme_new():

    file_path = r'E:\SHT\project\sas-web\src\main\webapp\src\saishi\scss'
    theme_color = []

    for path in IO_util.get_all_file(file_path):
        if skinFileReg.search(path):
            with open(path, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    result = skinReg.search(line)
                    if result:
                        theme_color.append(result.groups()[0])
                        break
    return theme_color


defaultColor = '#29d8c3'
print(defaultColor + ',' + ','.join(get_theme_new()))

