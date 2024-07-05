# P7. 流程控制语句

[文档地址](https://github.com/walter201230/Python/blob/master/Article/PythonBasis/python5/Cycle.md)

## 1. if

```python
# 非0
i = 10
if i:
    print('i != 0')
else:
    print('i = 0')

# 非空
s = ''
if s:
    print('s is not bland')
else:
    print('s is bland')

# 非空集
arr = [1]
if arr:
    print('arr is not bland')
else:
    print('arr is bland')

# 多个if else
j = 9
if j < 5:
    print('j < 5')
elif 5 < j < 10:
    print('j > 5 and j < 10')
elif j > 10:
    print('j > 10')
else:
    print(j)

# if 多条件判断
k = 12
if (j < 10 and k > 11) or (j < 10 and k > 11):
    print('j < 10 and k > 10')

# if 嵌套
if j < 10 and k > 11:
    if i:
        print("我是嵌套if")
else:
    print("第一层 else")
```

## 2. for

```python
# for 循环
for e in [1, 2, 3, 4, 5, 0, 6, 7, 8, 9]:
    if e:
        print(str(e) + ": Element not 0")

# range, 0 ~ x-1 的数字
for e in range(3):
    print(e)

# range(x, y) 左闭右开
for e in range(1, 4):
    print(e)

# range(x, y, z) 在一个左闭右开的区间内以z作为步跳
for e in range(1, 9, 3):
    print(e)

# while 循环
count = 1
sum1 = 0
while count <= 100:
    count = count + 1
    # 跳过当前循环
    if count <= 10:
        print("count=", count, ": 跳过当前循环")
        continue
    elif count == 90:
        print("count=", count, ": 推出循环")
        break
    else:
        sum1 = sum1 + count

print(sum1)

print()
print()

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()

print()
print()

# 判断是否是闰年
year = int(input("请输入一个年份: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0} 是闰年'.format(year))
else:
    print('{0} 不是闰年'.format(year))
```
[下一章: P8. 函数](../p8-function/README.md)

[上一章: P6. dict 和 set](../p6-dictionary/README.md)

