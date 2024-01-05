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