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
