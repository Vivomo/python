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

# test_search()
# test_group()
test_finditer()
