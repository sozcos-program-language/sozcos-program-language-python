# P17. 闭包

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python15/1.md)

> 场景: 函数内引用全局变量做累加\
> 原因: python 中, 全局变量被引用且修改, 该变量就会变成局部变量, 造成函数中没有进行定义变量就引用的错误\
> 异常: UnboundLocalError

```python
# 闭包问题复现
name = 0


def my_closure():
    for i in range(3):
        name = name + i
    return name


print(my_closure())
```


### 使用 global 来解决报错问题
```python
def my_closure2():
    global name
    for i in range(3):
        name = name + i
    return name


print(my_closure2())
```

## 使用闭包的方式解决全局变量引用修改问题

> Python 中, 要尽量避免修改全局变量, 因此使用闭包的方式类解决全局变量被应用修改的问题

```python
# 闭包方式
name = 0

def my_closure3(name):
    def my_closure4(m):
        nonlocal name
        for i in range(3):
            name = name + i + m
        return name

    return my_closure4


# 返回一个函数对象
f = my_closure3(name)
# 相当于调用 my_closure4 函数
print(f(2))
print(name)
```

[下一章: P18. 装饰器模式](../p18-decorator/README.md)

[上一章: P16. 正则表达式](../p16-regular/README.md)