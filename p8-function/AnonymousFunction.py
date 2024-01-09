"""
    匿名函数基本语法
    lambda [arg1 [,arg2,.....argn]]:expression
"""
var = lambda name, age: "我的名字叫{}, 今年{}岁".format(name, age)
print(var('小米', 46))

# 这主要在于 lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。
num2 = 100
sum1 = lambda num1: num1 + num2

num2 = 10000
sum2 = lambda num1: num1 + num2

print(sum1(1))
print(sum2(1))
