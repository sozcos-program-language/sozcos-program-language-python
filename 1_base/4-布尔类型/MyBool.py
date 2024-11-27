"""案例需求:
定义一个 1~10 的随机数字, 通过猜3次来确定数字, 给出数字大了, 小了的提示
"""
import random

num = random.randint(1, 10)

input_num = int(input("请输入1~10之间的数字: "))

if input_num == num:
    print("猜对了")
elif input_num > num:
    print("猜大了")
    input_num2 = int(input("请输入%s~10之间的数字: " % input_num))
    if input_num2 == num:
        print("猜对了")
    elif input_num2 > num:
        print("猜大了")
        input_num3 = int(input("请输入%s~10之间的数字: " % input_num2))
        if input_num3 == num:
            print("猜对了")
        else:
            print("猜小了")
else:
    print("猜小了")
    input_num2 = int(input("请输入1~10之间的数字: "))
    if input_num2 == num:
        print("猜对了")
    elif input_num2 > num:
        print("猜大了")
        input_num3 = int(input("请输入1~10之间的数字: "))
        if input_num3 == num:
            print("猜对了")
        else:
            print("猜小了")
    else:
        print("猜小了")





