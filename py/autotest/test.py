import json

with open('data.json', 'r', encoding='utf-8') as f:
    content = f.read()
    print(json.loads(content))
