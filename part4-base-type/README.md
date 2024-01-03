# Python 基本类型

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python2/Preface.md)

### 1. 字符串

```python
# 字符串可以使用 ‘’， “”， ‘’‘ ’‘’ 来表示， 作用是可以包含不同的内容符号
str1 = 'abc'

str2 = "a'b'c"

str3 = ''''a' "b" c'''
```

### 2.数字类型

```python
# integer 可以兼容整数以及浮点数
int1 = 1 - 1
int2 = 2 + 1
int3 = 1 / 2
int4 = 1 / 3

# 布尔
isRead = True
noRead = False

# 空
n1 = None

# 查看真是类型
print(type(int1))
```

### 3.数据类型转换

| 方法                     | 说明                              |
|------------------------|---------------------------------|
| int(x [,base ])        | 将x转换为一个整数                       |
| float(x )              | 将x转换到一个浮点数                      |
| complex(real [,imag ]) | 创建一个复数                          |
| str(x )                | 将对象 x 转换为字符串                    |
| repr(x )               | 将对象 x 转换为表达式字符串                 |
| eval(str )             | 用来计算在字符串中的有效 Python 表达式,并返回一个对象 |
| tuple(s )              | 将序列 s 转换为一个元组                   |
| list(s )               | 将序列 s 转换为一个列表                   |
| chr(x )                | 将一个整数转换为一个字符                    |
| unichr(x )             | 将一个整数转换为 Unicode 字符             |
| ord(x )                | 将一个字符转换为它的整数值                   |
| hex(x )                | 将一个整数转换为一个十六进制字符串               |
| oct(x )                | 将一个整数转换为一个八进制字符串                |

[下一章](../part5-array/README.md)