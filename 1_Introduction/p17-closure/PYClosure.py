# 闭包问题复现
name = 0


def my_closure():
    for i in range(3):
        name = name + i
    return name


# 使用 global 来解决报错问题
def my_closure2():
    global name
    for i in range(3):
        name = name + i
    return name


# 闭包方式
def my_closure3(name):
    def my_closure4(m):
        nonlocal name
        for i in range(3):
            name = name + i + m
        return name

    return my_closure4


# print(my_closure())
# print(my_closure2())

# 返回一个函数对象
f = my_closure3(name)
# 相当于调用 my_closure4 函数
print(f(2))
print(name)
