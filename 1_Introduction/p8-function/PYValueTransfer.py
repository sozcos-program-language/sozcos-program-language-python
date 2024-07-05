# 值传递问题, 变量b存储在栈内存中, 函数内的b变量存储在堆内存中, 并且2个内存没有声明赋值, 因此他们是没有关联的两个变量
def change_number(b):
    b = 1000
    return b


b = 1
# b = change_number(b), 当声明引用之后, b = 1000
change_number(b)
print(b)  # 1
