import os
from py.utils import IO_util

# writePath = r'E:\git\pythonCode\src\theme'
writePath2 = r'E:\SHT\project\sas-web\src\main\webapp\res\img\theme'
base64FilePath = r'E:\git\pythonCode\src\base64.txt'


def to_img():
    with open(base64FilePath, 'r', encoding='utf-8') as file:
        content = file.read()
        base64_arr = content.split('###')
        for i, base64str in enumerate(base64_arr):
            if i < 6:
                dir_path = os.path.join(writePath2, str(i + 1000001))
            else:
                dir_path = os.path.join(writePath2, str(i - 5 + 2000000))
            IO_util.base64_to_img(base64str[22:], os.path.join(dir_path, 'countdown_arc_bg.png'))


IO_util.clip(IO_util.img_to_base64(r'E:\chrome\double_arrow.png'))
