# 声明一个 list
name = ['abc', 'def', 'ghi', 'jkl']
# 声明一个多数据类型的 list
moreTypeArr = ['abnc', 123, 1.22, False]
# 读取 list 元素,  name[0:2], 左闭右开,意思就是从第 0 个开始取，取到第 2 个，但是不包含第 2 个
print(name[0:3])
# 添加元素
name.append(123)
# 删除元素
del name[3]
# 便利集合
for e in name: print(e)

print(name)
print(moreTypeArr)
