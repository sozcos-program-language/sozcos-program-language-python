"""
Python 的 for 循环不仅可以用在 list 或tuple 上，还可以作用在其他可迭代对象上。
也就是说，只要是可迭代的对象，无论有没有下标，都是可以迭代的。
"""
for e in "我是一个字符串":
    print(e, end=',')

print("\n*****************\n")

for e in [1, 23, 4, 5, 6]:
    print(e)

print("\n*****************\n")

# 使用迭代器来创建一个集合
i1 = iter("我是一个迭代器")
for e in i1:
    print(e)

print("\n*****************\n")

# next() 函数遍历迭代器
while True:
    try:
        print(next(i1))
    except StopIteration:
        break
