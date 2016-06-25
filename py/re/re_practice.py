import re
"""
正则练习题
"""


def re_practice1():
    """
    识别后续字符bat,bit,but,hat,hit,或hut
    """
    re.match(r'(b|h)(a|i|u)t', 'bat')

    """
    识别单个空格分隔的任意单词对
    """
    re.match(r'\w+\s\w+', 'hello world')

    """
    匹配有单个逗号或空格分隔的任意单词和单个字母
    """
    re.match(r'\w+[\s|,]\w+', 'I,m')

