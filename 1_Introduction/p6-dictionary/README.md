# P6. dict 和 set

## 1. dict

> 一种 MAP 数据结构

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

---

## 2. set

> 无序不重复元素集\
> py2 和 py3 语法上有不同?

```python
# 创建
set1 = {1, '12', 123, 1, '1'}
print(set1)

# 添加元素
set1.add('3')
print(set1)

# 交集
s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5}
s3 = s1 & s2
print(s3)

# 并集 （合并两个 set 集合的元素并去除重复的值）
s4 = s1 | s2
print(s4)

# 差集
s5 = s1 - s2
print(s5)
```

[下一章: P7. 流程控制语句](../p7-control-statemant/README.md)

[上一章: P5. List 和 Tuple](../p5-array/README.md)

