import json
import re
# with open('data.json', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(json.loads(content))

d = {'a': 1}

reg = re.compile(r'[^javascript]')
result = re.match(reg, 'javascript:;')
if result:
    print(result.groups())

