import os
import base64


def clip(s):
    command = 'echo ' + s.strip() + '| clip'
    os.system(command)
    print('Copy successful')


def img_to_base64(file_path):
    with open(file_path, 'rb') as img:
        return 'data:image/png;base64,' + base64.b64encode(img.read()).decode('utf-8')

while True:
    filePath = input('Img Path:')
    if filePath == '886':
        break
    else:
        clip(img_to_base64(filePath))
