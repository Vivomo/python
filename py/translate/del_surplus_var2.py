import os
import re
import copy
from py.utils import IO_util
from py.translate import line as L


enPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
zhPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\zh'
varReg = re.compile(r'(l_\w+)\s?=\s?".+?"')

for path in [enPath, zhPath]:
    for f in IO_util.get_all_file(path):
        with open(f, 'r', encoding='utf-8') as file:
            varArr = []
            delArr = []
            lines = file.readlines()
            lines.reverse()
            length = len(lines)
            for i, l in enumerate(lines):
                result = re.search(varReg, l)
                if result:
                    var = result.groups()[0]
                    if var in varArr:
                        delArr.append(length - i)
                    else:
                        varArr.append(var)
            IO_util.del_file_lines(f, delArr)
            # print(f, '-'.join(delArr))
