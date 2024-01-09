# 函数默认参数, 默认值参数只能在无默认值参数后面声明
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


######################################

# 关键字参数: 参数需要根据顺序来进行传参, 避免引起传错值导致的问题, 在 Python 中，可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序，这被称之为关键字参数。
def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return


print_user_info(name='两点水', age=18, sex='女')
print_user_info(name='两点水', sex='女', age=18)


######################################

# 不定长参数, 在参数前边加星号 *, 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
# def print_user_info(name, age, *var): 不定长参数, 与位置参数使用会报错
def print_user_info(name, age, **var):  # 位置+不定长参数
    print("name={}".format(name))
    print("age={}".format(age))
    for e in var:
        print("var={}".format(e))


# print_user_info('小明', 18, '喜欢吃路边摊', 12, 12.1)
print_user_info(name='小明', age=18, var=('喜欢吃路边摊', 12, 12.1))


######################################
# 强制使用位置参数, * 后面是强制使用位置参数的声明
def print_user_info(name, *, age, sex):
    print("name={}".format(name))
    print("age={}".format(age))
    print("sex={}".format(sex))
    return


print_user_info('小明:', age=12, sex='男')
