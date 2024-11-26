
print("我是%s, 今年%s岁" % (name, age))


# 字符串的精度控制
num1 = 11.2
num2 = 11.345
print("补位操作 %s ==> %5d" % (num1, num1))
print("补位四舍五入操作 %s ==> %1.2f" % (num2, num2))
print("四舍五入操作 %s ==> %.2f" % (num2, num2))


# 字符串的快速格式化
print(f"我的名字是{name}, 今年{age}岁")