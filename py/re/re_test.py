import re

"""
re 模块的测试
"""

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

