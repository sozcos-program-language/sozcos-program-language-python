# P13. Python 枚举

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python11/Preface.md)

```python
# 定义一个枚举类
from enum import Enum

Sex = Enum('sex', ('man', 'woman'))

for name, m in Sex.__members__.items():
    print(name, m, m.value)

# 枚举成员引用
print(Sex.man)
```

> @unique 装饰器可以帮助我们检查保证没有重复值

```python
from enum import Enum, unique

@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
```


[下一章: P14. 元类](../p14-metaclass/README.md)

[上一章: P12. 魔法函数](../p12-megic-function/README.md)
