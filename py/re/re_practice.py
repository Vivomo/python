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


def re_practice2():
    """
    匹配python标识符的集合
    """
    re.match('[a-zA-Z_$]\w*', 'python')
    """
    匹配美国街道名称
    """
    re.match('\d+(\s\w+)+', '10082 Da le me')
    """
    匹配www起始 .com结尾的域名
    """
    re.match(r'www://(\w+.)+?\w+', 'www://www.bing.com')


def re_practice3():
    """
    匹配email
    """
    re.match('(\w+.)*\w+@(\w+.)*\w+.(\w+.)*\w+', '929992114@qq.com')
    """
    匹配url
    TODO 待完善
    """
    re.match(r'(https?://)?(\w+.)*\w+')
    """
    python type 返回值 eg. <type 'a_b'>
    """
    re.match(r'<type\s\'\w+\'>', r'<type \'a_b\'>')
    

