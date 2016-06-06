import os
import re


def file_to_map(file_path):
    file_map = {}
    p = re.compile('\.icon\w+')

    with open(file_path, 'r') as file:
        for line in file.readlines():
            m = p.match(line)
            if m is not None:
                key = m.group()[1:]
                value = key[:4] + '-' + key[4:].lower()
                file_map[key] = value
    return file_map


def get_all_file(file_path):
    file_list = []

    for p, d, f in os.walk(file_path):
        for f1 in f:
            file_list.append(os.path.join(p, f1))
    return file_list


def replace_file_word(file_list, word_map):
    for path in file_list:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        for key, value in word_map.items():
            content = content.replace(key, value)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

# targetPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\waptemplate\default'
targetPath2 = r'E:\SHT\project\sas-web\src\main\webapp\src\m\js'
fileList = get_all_file(targetPath2)
iconMap = file_to_map('../src/targetfile.txt')
replace_file_word(fileList, iconMap)


