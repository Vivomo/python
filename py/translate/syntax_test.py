import re


s1 = '123123123'
result = re.findall('4', s1)
print(result)
for item in result:
    print(item)

testStr = '12312312  lang_name = \'global\''
langNameExp = r'lang_name\s?=\s?[\'\"]\w+[\'\"]'
# langNameArr = re.findall(langNameExp, testStr)
# if langNameArr:
#     # langName = re.split(r'\s', re.sub(r'^[a-zA-Z]', langNameArr[0], ' '))
#     langName = re.split(r'\s+', re.sub(r'\W', ' ', langNameArr[0]).strip())
#     print(langName)

#
# d1 = {'a': 1, 'b': 1}
# d2 = {'b': 2}
# d3 = dict(d1.items() | d2.items())
# print(d3)

l = ['asd', 'asdasd', 'as', 'a']

l.sort(key=len, reverse=True)
print(l)
