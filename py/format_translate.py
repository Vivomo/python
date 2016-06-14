import os
import re


EnglishExp = '"[\w\s]+"'
lineNumExp = r'<#--\d+-->'
commentExp = r'<#--.+?-->'
commentStartToken = '<#--'
commentEndToken = '-->'
commentMarkExp = r'[<>#-]'
prefix = r'l_'


class Line(object):
    def __init__(self, line):
        en_arr = re.findall(EnglishExp, line)
        if en_arr:
            self.en = en_arr[0].replace('"', '')
        else:
            self.en = ''
        self.name = re.sub(r'\s+', '_', self.en.lower())

        comment_arr = re.findall(commentExp, line)
        if comment_arr:
            self.num = filter_comment(comment_arr[0])
            self.ch = filter_comment(comment_arr[1].replace(commentMarkExp, ''))
        else:
            self.num = ''
            self.ch = ''

    def __str__(self):
        return '\t[en:%s][ch:%s][num:%s]' % (self.en, self.ch, self.num)

    def is_legal(self):
        return self.name != ''


def get_all_file(file_path):
    file_list = []

    for p, d, f in os.walk(file_path):
        for f1 in f:
            file_list.append(os.path.join(p, f1))
    return file_list


def filter_comment(filter_str):
    return filter_str.replace(commentStartToken, '').replace(commentEndToken, '')


def format_line(line):
    """
    :line l_78543943 = "View all" <#--78543943--> <#--查看全部-->
    :return l_view_all = "View all" <#--78543943--> <#--查看全部-->
    """
    en = re.findall(EnglishExp, line)
    return en

print(format_line('123 213"The Test"')[0])
print(format_line('l_xxx'))

print(Line('l_78543943 = "View all" <#--78543943--> <#--查看全部-->'))
