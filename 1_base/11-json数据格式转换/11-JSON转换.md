# JSON 转换

### [视频地址](https://www.bilibili.com/video/BV1qW4y1a7fU?spm_id_from=333.788.videopod.episodes&vd_source=b5c04f54b8a7ce0b4d5deef9989f7f9f&p=100)

使用 json 包转换和解析json

```pycon
import json

# 字典转换为json字符串
data = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
json_str = json.dumps(data)
print(json_str)

# json字符串转换为字典
json_str = '{"name": "Bob", "age": 30, "city": "Shanghai"}'
data = json.loads(json_str)
print(data)
```