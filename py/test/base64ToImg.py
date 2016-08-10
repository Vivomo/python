import os
import base64
from py.utils import IO_util

writePath = r'E:\git\pythonCode\src\theme'
base64FilePath = r'E:\git\pythonCode\src\base64.txt'

with open(base64FilePath, 'r', encoding='utf-8') as file:
    content = file.read()
    base64Arr = content.split('###')
    for i, base64str in enumerate(base64Arr):
        # l = len(base64str)
        # if l % 3 != 0:
        #     base64str += (3 - l % 3) * '='
        dir_path = os.path.join(writePath, str(i + 1))
        IO_util.base64_to_img(base64str[22:], os.path.join(dir_path, 'countdown_arc_bg.png'))

