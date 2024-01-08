# 自定义函数
# def 函数名(参数1，参数2....参数n):
#     函数体
#     return 语句

def my_function(var, var2):
    print("var={}".format(var), "var2={}".format(var2))
    return var, var2 # 这里其实是返回了一个 tuple


v1, v2 = my_function(91, 1.98)
print(v1)
print(v2)
