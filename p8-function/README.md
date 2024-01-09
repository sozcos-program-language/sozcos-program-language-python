# P8. 函数

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python6/Preface.md)

## 1.自定义函数
> def 函数名(参数1，参数2....参数n):\
     函数体\
     return 语句

```python
def my_function(var, var2):
    print("var={}".format(var), "var2={}".format(var2))
    return var, var2 # 这里其实是返回了一个 tuple


v1, v2 = my_function(91, 1.98)
print(v1)
print(v2)
```

## 2.函数参数

### 2.1 默认参数
> 默认值参数只能在无默认值参数后面声明

```python
def my_default_value_function(d3, d1='default'):
    if d3:
        print('d3 is None')
    print("d1={}".format(d1))
    print("d3={}".format(d3))
    return


my_default_value_function(12)

# 声明一个超类
_no_value = object()


# 判断是否给某个参数赋值
def print_info(a, b=_no_value):
    if b is _no_value:
        print('b 没有赋值')
    return
```

### 2.2 位置参数
> 参数需要根据顺序来进行传参, 避免引起传错值导致的问题, 在 Python 中，可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序，这被称之为关键字参数。

```python
def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return


print_user_info(name='两点水', age=18, sex='女')
print_user_info(name='两点水', sex='女', age=18)

# 强制使用位置参数, * 后面是强制使用位置参数的声明
def print_user_info(name, *, age, sex):
    print("name={}".format(name))
    print("age={}".format(age))
    print("sex={}".format(sex))
    return


print_user_info('小明:', age=12, sex='男')
```

### 2.3 不定长参数
> 在参数前边加星号 *, 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。

```python
# def print_user_info(name, age, *var): 不定长参数, 与位置参数使用会报错
def print_user_info(name, age, **var):  # 位置+不定长参数
    print("name={}".format(name))
    print("age={}".format(age))
    for e in var:
        print("var={}".format(e))


 print_user_info('小明', 18, '喜欢吃路边摊', 12, 12.1)
print_user_info(name='小明', age=18, var=('喜欢吃路边摊', 12, 12.1))
```

### 2.4 函数值问题
> 值传递问题, 变量b存储在栈内存中, 函数内的b变量存储在堆内存中, 并且2个内存没有声明赋值, 因此他们是没有关联的两个变量

```python
def change_number(b):
    b = 1000
    return b


b = 1
# b = change_number(b), 当声明引用之后, b = 1000
change_number(b)
print(b)  # 1
```

### 2.5 匿名函数
>     匿名函数基本语法\
>     lambda [arg1 [,arg2,.....argn]]:expression\
> 注意：尽管 lambda 表达式允许你定义简单函数，但是它的使用是有限制的。 你只能指定单个表达式，它的值就是最后的返回值。也就是说不能包含其他的语言特性了， 包括多个语句、条件表达式、迭代以及异常处理等等

```python
var = lambda name, age: "我的名字叫{}, 今年{}岁".format(name, age)
print(var('小米', 46))
```

> 这主要在于 lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。

```python
num2 = 100
sum1 = lambda num1: num1 + num2

num2 = 10000
sum2 = lambda num1: num1 + num2

print(sum1(1)) # 10001
print(sum2(1)) # 10001
```

[下一章: P9. 迭代器和生成器](../p9-Iterators/README.md)

[上一章: P7. 流程控制语句](../p7-control-statemant/README.md)