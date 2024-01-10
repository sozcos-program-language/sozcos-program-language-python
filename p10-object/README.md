# P10. 面向对象

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python8/2.md)

## 1.类
> 声明一个类:
> class ClassName():
>     <statement-1>
>     .
>     <statement-N>

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