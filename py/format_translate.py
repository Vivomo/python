import os
import re

"""
这里的英文可能是一句话, 可能包含- . '
但英文会被双引号引起来, 所以正则是这样的
"""
EnglishExp = '".+?"'
lineNumExp = r'<#--\d+-->'
commentExp = r'<#--.+?-->'
commentStartToken = '<#--'
commentEndToken = '-->'
# commentMarkExp = r'[<>#-]'
enPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
writePathZh = r'E:\git\pythonCode\test\translate\write\zh'
writePathEn = r'E:\git\pythonCode\test\translate\write\en'
prefix = r'l_'


class Line(object):
    def __init__(self, line):
        self.line = line
        en_arr = re.findall(EnglishExp, line)
        if en_arr:
            self.en = en_arr[0].replace('"', '')
            self.name = 'l_'+re.sub(r'\s+', '_', self.en.lower())
        else:
            self.en = ''
            self.name = ''

        comment_arr = re.findall(commentExp, line)
        if comment_arr and len(comment_arr) == 2:
            self.num = filter_comment(comment_arr[0])
            self.ch = filter_comment(comment_arr[1])
        else:
            self.num = ''
            self.ch = ''

    def __str__(self):
        return '\t[en:%s][ch:%s][num:%s]' % (self.en, self.ch, self.num)

    def is_legal(self):
        return self.name != '' and self.en != '' and self.ch != ''

    def to_en(self):
        if self.is_legal():
            return '%s = "%s" <#--%s--> <#--%s-->' % (self.name, self.en, self.num, self.ch)
        else:
            return self.line.replace('\n', '')

    def to_ch(self):
        if self.is_legal():
            return '%s = "%s" <#--%s-->' % (self.name, self.en, self.num)
        else:
            return self.line.replace('\n', '')


def get_all_file(file_path):
    file_list = []

    for p, d, f in os.walk(file_path):
        for f1 in f:
            file_list.append(os.path.join(p, f1))
    return file_list


def filter_comment(filter_str):
    return filter_str.replace(commentStartToken, '').replace(commentEndToken, '')


def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def format_file(file_path):
    en_lines = []
    # zh_lines = []
    file_name = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as read_file:
        for item in read_file.readlines():
            try:
                line = Line(item)
                en_lines.append(line.to_en())

            except Exception as e:
                en_lines.append(item)
                print(e)
                print('error file is %s and the content of line is %s' % (file_name, item))
            # zh_lines.append(line.to_ch())

    # write_to_file(os.path.join(writePathZh, file_name), '\n'.join(zh_lines))
    write_to_file(os.path.join(enPath, file_name), '\n'.join(en_lines))


def format_file2(file_path):
    """
        去重
    """
    word_set = set()
    lines = []
    file_name = os.path.basename(file_path)
    if file_name != 'l_global.ftl' and file_name.find('e') == 0:
        with open(file_path, 'r', encoding='utf-8') as read_file:
            for item in read_file.readlines():
                line = Line(item)
                if line.ch:
                    if line.ch not in word_set:
                        word_set.add(line.ch)
                        lines.append(line.to_en())
                else:
                    lines.append(line.to_en())

        write_to_file(os.path.join(enPath, file_name), '\n'.join(lines))
    return word_set

testFilePath = r'E:\git\pythonCode\test\translate\write\en\event_order.ftl'
globalFilePath = ''
globalSet = format_file2(globalFilePath)
format_file2(testFilePath)
#
# for path in get_all_file(enPath):
#     format_file(path)
