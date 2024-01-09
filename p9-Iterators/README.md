# P9. 迭代器和生成器

## 1.迭代器
> Python 的 for 循环不仅可以用在 list 或tuple 上，还可以作用在其他可迭代对象上。\
> 也就是说，只要是可迭代的对象，无论有没有下标，都是可以迭代的。

```python
for e in "我是一个字符串":
    print(e, end=',')


for e in [1, 23, 4, 5, 6]:
    print(e)

    
# 使用迭代器来创建一个集合
i1 = iter("我是一个迭代器")
for e in i1:
    print(e)

    
# next() 函数遍历迭代器
while True:
    try:
        print(next(i1))
    except StopIteration:
        break
```

## 2.生成器 和生成式

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python7/4.md)

### 2.1 生成式

> 生成式 \
> [expr for iter_var in iterable]\
> [expr for iter_var in iterable if cond_expr]

```python
# 循环一个区间内容, 根据算法生成一个新的list
arr1 = [x * x for x in range(1, 8)]
print(arr1)

# 循环一个区间元素, 元素满足 if 判断才向集合添加元素
arr2 = [x * x for x in range(1, 8) if x % 2 == 0]
print(arr2)
```

### 2.2 生成器
> 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素
> 就不必创建完整的 list，从而节省大量的空间, 这就是生成器需要处理的问题, 生成器是一个返回迭代器的函数，只能用于迭代操作
> 生成器的最好的应用是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。因为这样会耗很大的资源。
> 
> 生成器可以理解成是一个序列, 用到的时候才会去计算下一个元素值, 跟生成式的区别是 [] -> ()

```python
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
```

[下一章: P10. 面向对象](../p10-object/README.md)

[上一章: P8. 函数](../p8-function/README.md)





