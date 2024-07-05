# 创建
set1 = {1, '12', 123, 1, '1'}
print(set1)

# 添加元素
set1.add('3')
print(set1)

# 交集
s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5}
s3 = s1 & s2
print(s3)

# 并集 （合并两个 set 集合的元素并去除重复的值）
s4 = s1 | s2
print(s4)

# 差集
s5 = s1 - s2
print(s5)