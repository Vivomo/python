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
        if comment_arr:
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
            return self.line

    def to_ch(self):
        if self.is_legal():
            return '%s = "%s" <#--%s-->' % (self.name, self.en, self.num)
        else:
            return self.line


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
    with open(file_path, 'r', encoding='utf-8') as read_file:
        file_name = os.path.basename(read_file.name)
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


testFilePath = r'E:\git\pythonCode\test\translate\write\en\event_order.ftl'

format_file(testFilePath)

for path in get_all_file(enPath):
    format_file(path)
