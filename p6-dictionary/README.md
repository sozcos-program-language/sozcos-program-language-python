# P6. 字典

## 1. 字典,一种MAP数据乐星

```python
# 声明字典
dictMap = {'k': 'v', 'k1': 'k2'}
print(dictMap['k'])

# 新增元素
dictMap['k2'] = '123456'
print(dictMap)

# 删除元素
del dictMap['k']
print(dictMap)
```

## 2、dict （字典） 的函数和方法

| 方法和函数          | 描述                       |
|----------------|--------------------------|
| len(dict)      | 计算字典元素个数                 |
| str(dict)      | 输出字典可打印的字符串表示            |
| type(variable) | 返回输入的变量类型，如果变量是字典就返回字典类型 |
| dict.clear()   | 删除字典内所有元素                |
| dict.copy()    | 返回一个字典的浅复制               |
| dict.values()  | 以列表返回字典中的所有值             |
| popitem()      | 随机返回并删除字典中的一对键和值         |
| dict.items()   | 以列表返回可遍历的(键, 值) 元组数组     |

[上一章：P5. List 和 Tuple](../p5-array/README.md)

