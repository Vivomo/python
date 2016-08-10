from py.utils import IO_util
import re

# 获取theme4
filePath = r'E:\SHT\project\sas-web\src\main\webapp\src\default\scss'
theme4Reg = re.compile(r'\$theme4:\s?(#\w+)')
themeColor = []

for path in IO_util.get_all_file(filePath):
    if path.find('theme') != -1:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                result = theme4Reg.search(line)
                if result:
                    themeColor.append(result.groups()[0])
                    break

print(','.join(themeColor))
