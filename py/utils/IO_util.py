import os


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
