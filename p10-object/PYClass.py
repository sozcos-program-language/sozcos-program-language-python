"""
声明一个类:
class ClassName():
    <statement-1>
    .
    <statement-N>
"""


class MyClass():
    # 类成员
    var1 = 100
    var2 = 10.1
    var3 = '可乐'

    def func1():
        print("abc")


print(MyClass.var1)
print(MyClass.var2)
print(MyClass.var3)

MyClass.func1()
