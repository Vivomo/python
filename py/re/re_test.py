import re
import os
"""
re 模块的测试
"""


def test_compile():
    str1 = 'food'
    m1 = re.match('foo', str1)
    print(m1)
    print(m1.group())
    print(m1.groups())

    m = re.compile('foo')
    m2 = m.match(str1)
    print(m2)
    print(m2.group())
    print(m2.groups())


def test_search():
    m = re.match('foo', 'seafood')
    print(m)
    m1 = re.search('foo', 'seafood food')
    print(m1)
    print(m1.group())
    print(m1.groups())


def test_group():
    m = re.match('ab', 'ab')
    print(m.group())
    print(m.groups())

    m = re.match('(ab)', 'ab')
    print(m.group())
    print(m.groups())

    m = re.match('(a)(b)', 'ab')
    print(m.group())
    print(m.groups())

    m = re.match('(a(b))', 'ab')
    print(m.group())
    print(m.groups())


def test_finditer():
    """
    python3  的迭代器还不会用 finditer 暂时pass
    :TODO
    """
    th_reg = r'(th\w) and (th\w+)'
    s = 'This and that'
    result = re.findall(th_reg, s, re.I)
    print(result)
    result2 = re.finditer(th_reg, s, re.I).__next__().group(1)
    print(result2)


def test_subn():
    s = 'I love X,X...'
    print(re.sub('X', 'susu', s))
    print(re.subn('X', 'susu', s))


def test_reg_expand():
    print(re.findall(r'(?i)yes', 'yes? Yes. YES!!'))
    print(re.findall(r'(?im)(^th[\w ]+)', """
The line is first,
another line,
that line, it's the best
    """))
    print(re.search(r'''(?x)
    \((\d{3})\)
    [ ]
    (\d{3})
    -
    (\d{4})
''', '(800) 555-1212').groups())

    print(re.findall(r'http://(?:\w+\.)*(\w+\.com)',
                     'http://google.com http://www.google.com http://code.google.com'))
    print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
              '(800) 555-1212').groupdict())
    print(re.search(r'(?P<name>l_\w+) = "(?P<en>.+?)" <#--(?P<num>\d+)--> <#--(?P<ch>.+?)-->', 'l_delete_order = "Delete order" <#--36436328--> <#--删除订单-->').groupdict())


def test_reg_expand2():
    print(re.findall(r'\w+(?= vimo)', '''
    abc vimo
    efg
    hig vimo
    '''))
    print(re.findall(r'(?m)^\s+(?!vimo|tizo)(\w+)', '''
    abc@qq.com
    vimo@qq.com
    tizo@qq.com
    7890qqewq
    '''))
    print(['%s@aw.com' % e.group(1) for e in re.finditer(r'(?m)^\s+(?!vimo|tizo)(\w+)', '''
    abc@qq.com
    vimo@qq.com
    tizo@qq.com
    7890qqewq
    ''')])


def test_other():
    with os.popen('tasklist /nh', 'r') as f:
        for eachline in f:
            print(re.findall(r'([\w.]+(?:[\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
                             eachline.rstrip()))
# test_search()
# test_group()
# test_finditer()
# test_subn()
# test_reg_expand()
# test_reg_expand2()
test_other()
