import os
import re
from py.utils import IO_util


os.rename(r'E:\git\pythonCode\src\new 1.txt', r'E:\git\pythonCode\src\new2.txt')

def rename1(file_path, reg1, reg2):
    pass

d = input('目录:')
filePaths = IO_util.get_all_file(d)
print(filePaths)
reg1 = re.compile(input('正则输入:'))

re.sub()