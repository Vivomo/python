import os
import base64


def get_all_file(file_path):
    """
    获取一个路径下的所有文件
    :return 文件列表
    """
    file_list = []

    for p, d, f in os.walk(file_path):
        for f1 in f:
            file_list.append(os.path.join(p, f1))
    return file_list


def write_to_file(file_path, content):
    """
    将内容写入文件
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def del_file_lines(file_path, del_lines):
    """
    将文件的指定行删除, 首行不是0, 是1
    """
    if isinstance(del_lines, list):
        with open(file_path, 'r', encoding='utf-8') as f:
            write_c = []
            for i, line in enumerate(f.readlines()):
                if i + 1 not in del_lines:
                    write_c.append(line)
        write_to_file(file_path, ''.join(write_c))


def base64_to_img(base64str, file_path):
    """
    将一个base64字符串转为图片存入指定路径
    :param base64str: base64字符串
    :param file_path: 图片写入的路径
    :return:
    """
    img_data = base64.b64decode(base64str)
    file = open(file_path, 'wb')
    file.write(img_data)
    file.close()
