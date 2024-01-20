"""
生成式
[expr for iter_var in iterable]
[expr for iter_var in iterable if cond_expr]
"""
# 循环一个区间内容, 根据算法生成一个新的list
arr1 = [x * x for x in range(1, 8)]
print(arr1)

# 循环一个区间元素, 元素满足 if 判断才向集合添加元素
arr2 = [x * x for x in range(1, 8) if x % 2 == 0]
print(arr2)

for e in range(1, 10, 2):
    print("指定步长的区间元素定义: e = {}".format(e))

"""
generator 生成器

如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素
就不必创建完整的 list，从而节省大量的空间, 这就是生成器需要处理的问题, 生成器是一个返回迭代器的函数，只能用于迭代操作
生成器的最好的应用是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。因为这样会耗很大的资源。

生成器可以理解成是一个序列, 用到的时候才会去计算下一个元素值, 跟生成式的区别是 [] -> ()
"""
# 创建一个生成器
gt = (x * x for x in range(1, 4))

for e in gt:
    print("e=", e)


# 生成器只能迭代一次, 因此要使用函数形式实现生成器, yield 是声明生成器的关键字
def my_function():
    for i in range(10):
        yield i


print(my_function())


# -*- coding: UTF-8 -*-
def odd():
    print('step 1')
    yield (1)
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
print(next(o))
print(next(o))
print(next(o))
