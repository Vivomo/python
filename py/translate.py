import re
import os
import random

readPath = r'E:\git\pythonCode\test\translate\read'
writePath = r'E:\git\pythonCode\test\translate\write'
chineseReg = u"[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+"


def get_all_file(file_path):
    file_list = []

    for p, d, f in os.walk(file_path):
        for f1 in f:
            file_list.append(os.path.join(p, f1))
    return file_list


def format_assign(zh):
    _r = int(random.random() * 100000000)
    return '\tl_%d = "%s" <#--%d-->\n' % (_r, zh, _r)


def fetch_chinese(file_list):

    for path in file_list:
        with open(path, 'r', encoding='utf-8') as r_file:
            write_file_path = os.path.join(writePath, os.path.basename(r_file.name))
            with open(write_file_path, 'w', encoding='utf-8') as w_file:
                w_content = []
                temp_content = set().add('<#assign'+'\n')
                for line in r_file.readlines():
                    zh_arr = re.findall(chineseReg, line)
                    for zh in zh_arr:
                        temp_content.add(zh)

                map(format_assign, temp_content)
                w_content.append('>')
                w_file.write(''.join(w_content))


fileList = get_all_file(readPath)
fetch_chinese(fileList)




