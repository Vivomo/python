import os
import re
from py.utils import IO_util

enPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
# zhPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\zh'
lineReg = re.compile(r'\w+\s*:\s*\'.+?\'')


def capitalize_line(line):
    index = line.find('\'')
    # index = line.find('"')
    return line[:index+1] + line[index+1].upper() + line[index+2:]


def capitalize_file(file_path):
    line_arr = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            result = re.search(lineReg, line)
            if result:
                line_arr.append(capitalize_line(line))
            else:
                line_arr.append(line)
    IO_util.write_to_file(file_path, ''.join(line_arr))

# for p1 in IO_util.get_all_file(enPath):
#     capitalize_file(p1)
# capitalize_file(r'E:\SHT\project\sas-web\src\main\webapp\src\js\language\language.js')

