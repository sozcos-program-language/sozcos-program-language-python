# P10. 面向对象

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python8/2.md)

## 1.类

> 声明一个类:
> class ClassName():
> <statement-1>
> .
> <statement-N>

```python
class MyClass():
    # 类成员
    var1 = 100
    var2 = 10.1
    var3 = '可乐'

    @classmethod  # 此注解作用是让类函数可以访问类成员变量
    def func1(cls, age):
        print("我喜欢{}".format(cls.var3))
        # 添加函数参数, 在调用端可以直接传此参数
        print("今年{}岁".format(str(age)))


print(MyClass.var1)
print(MyClass.var2)
print(MyClass.var3)

MyClass.func1(18)
```

## 2.修改和增加类属性

```python
# 从内部添加和修改类属性
class ClassA():
    var1 = '小明'

    @classmethod
    def m1(cls):
        cls.var1 = input("请输入var1新值:")
        print("var1={}".format(cls.var1))
        cls.var2 = input("var2 新值=")
        print("var2={}".format(cls.var2))


ClassA.m1()


# 从外部修改和增加类属性
class ClassB():
    var1 = 10

    @classmethod
    def m2(cls):
        print("var1={}".format(cls.var1))


ClassB.var2 = input("classB.var2=")
print(ClassB.var2)
```

## 3.类和对象

```python
# 声明一个对象
class ClassA():
    v1 = '我是一个对象'

    # 类方法不需要用 @classmethod 来声明, cls 改成 self 或者其他字母都行 只不过 cls 和 self 都是编程习惯, self 是所有类方法位于首位、默认的特殊参数。
    def m1(self):
        print(self.v1)


class_a = ClassA()
class_a.m1()


# 示例对象的变量以及方法都可以被重写和覆盖

def new_fun(self):
    print("我是一个新函数")


ClassA.v1 = '我是一个新变量'
ClassA.m1 = new_fun

class_a.m1()
print(class_a.v1)

# 但是类方法不能改变
class_a.m1 = new_fun
class_a.m1()
```

## 4.初始化函数

> 初始化函数在对象实例化的时候会被调用, 也叫构造函数\
> 第一个参数一定要写上 self\
>
> def __init__(self,[...):

```python
class Person(object):

    # 构造参数
    def __init__(self, v1):
        print("__init__ success")
        print(v1)

    # 析构函数, 示例被销毁的时候调用
    def __del__(self):
        print("__del__ success")


person = Person("我是第二个参数")

# 销毁实例
del person
```

## 5.继承

### 单继承

> **语法**:  
> class ClassName(BaseClassName):  
> <statement-1>  
> .  
> <statement-N>

### 多继承

> 多继承有一点需要注意的：若是父类中有相同的方法名，而在子类使用时未指定，  
> python 在圆括号中父类的顺序，从左至右搜索 ， 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

> class ClassName(Base1,Base2,Base3):  
> <statement-1>  
> .  
> <statement-N>

```python
# 继承
class Man(object):
    def __init__(self):
        print("Man is init")


class Person(object):
    def __init__(self):
        print("I am a person")


class Student(Person, Man):
    def __init__(self):
        super().__init__()
        print("I am a student")


s1 = Student()
```

## 6.多态

> 多态, 同一个事件应为不同的对象做出不同的响应

```python
# 多态
class User(object):
    def __init__(self, name):
        self.name = name

    def printUser(self):
        print('Hello !' + self.name)


class UserVip(User):
    def printUser(self):
        print('Hello ! 尊敬的Vip用户：' + self.name)


class UserGeneral(User):
    def printUser(self):
        print('Hello ! 尊敬的用户：' + self.name)


def printUserInfo(user):
    user.printUser()


if __name__ == '__main__':
    userVip = UserVip('两点水')
    printUserInfo(userVip)
    userGeneral = UserGeneral('水水水')
    printUserInfo(userGeneral)
```

## 7.类访问控制

> 用双下划线声明私有属性, py 的所有属性都是公共属性, 靠人为避免

```python
class UserVip(object):

    def __init__(self, name, age):
        super().__init__(name)
        self.__name = name
        self.__age = age

    def __pri_md__(self, other):
        print("我是私有方法")

    def printUser(self):
        print('Hello ! 尊敬的Vip用户：' + self.name)
```

> 类的专有方法：

| 方法             | 说明            |
|----------------|---------------|
| `__init__`     | 构造函数，在生成对象时调用 |
| `__del__ `     | 析构函数，释放对象时使用  |
| `__repr__ `    | 打印，转换         |
| `__setitem__ ` | 按照索引赋值        |
| `__getitem__`  | 按照索引获取值       |
| `__len__`      | 获得长度          |
| `__cmp__`      | 比较运算          |
| `__call__`     | 函数调用          |
| `__add__`      | 加运算           |
| `__sub__`      | 减运算           |
| `__mul__`      | 乘运算           |
| `__div__`      | 除运算           |
| `__mod__`      | 求余运算          |
| `__pow__`      | 乘方            |


[下一章: P11. Python 模块](../p11-module/README.md)

[上一章: P9. 迭代器和生成器](../p9-Iterators/README.md)