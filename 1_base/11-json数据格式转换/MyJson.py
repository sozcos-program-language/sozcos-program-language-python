import json

info = {"name": "大力", "age": 30, "city": "New York"}
# 不适用 acoll 编码, 直接输出
json_str = json.dumps(info, ensure_ascii=False)
print(json_str)

str = '{"name": "大理", "age": 30, "city": "New York"}'
loads = json.loads(str)
print(loads['name'])
