# P12. 魔法函数

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python10/1.md)

> 使用 `__xxx__` 双下划线修饰的的函数称为: magic method , 魔法方法\
> 可以使用 py 自带的 dir() 方法来查看类的魔法方法

```python
class Man(object):
    pass


# 查看类的魔法方法
print(dir(Man()))
```

## 1.类的创建过程:

> 类会先调用 `__new__` 函数类创建一个对象, 这个函数返回了一个对象\
> 然后再调用 `__init__` 函数初始化对象\
> 通过打印的结果来看，我们就可以知道一个类创建的过程是怎样的了，先是调用了 `__new__`
> 方法来创建一个对象，把参数传给 `__init__` 方法进行实例化。

```python
class Man(object):
    def __new__(cls, *args, **kwargs):
        print('调用了new函数')
        return super().__new__(cls)  # 如果没有返回实例对象,那么则会接受到一个 none 值

    def __init__(self, name):
        print('调用了init函数', 'name={}'.format(name))


# 查看类的魔法方法
print(Man('param'))
```

> 其实在实际开发中，很少会用到 `__new__` 方法，除非你希望能够控制类的创建。通常讲到 `__new__` ，都是牵扯到 metaclass(元类)的。

[P13. Python 枚举](../p13-enums/README.md)

[上一章: P11. Python 模块](../p11-module/README.md)
