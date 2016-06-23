import re

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

# test_search()
# test_group()
# test_finditer()
# test_subn()
test_reg_expand()
