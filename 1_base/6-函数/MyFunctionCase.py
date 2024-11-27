"""
定义一个隐含卡余额变量: money,
定义一个用户姓名变量: name

定义如下函数:
    - 查询余额
    - 存款函数
    - 取款函数
    - 主菜单函数

要求:
    - 程序启动后要求输入客户姓名
    - 查询余额, 存款, 取款后都会返沪主菜单
    - 存款, 取款后, 都应显示一下当前余额
    - 客户选择退出或输入错误, 程序会退出, 否则一直运行
"""

name = input("请输入您的姓名:")
money = 100

"""
查询余额
"""
def query_balance():
    print(f"您好, {name}, 您的余额为:{money}")

"""
存款函数
"""
def deposit():
    global money
    money += int(input("请输入存款金额:"))
    print(f"您好, {name}, 您的余额为:{money}")


"""
取款
"""
def withdraw():
    global money
    money -= int(input("请输入取款金额:"))
    print(f"您好, {name}, 您的余额为:{money}")

"""
主菜单
"""
def main_menu():
    content = f"-----------主菜单-----------\n{name}, 你好, 欢迎来到ATM, 请选择操作\n查询余额: 输入[1]\n存款: 输入[2]\n取款: 输入[3]\n退出: 输入[4]\n请输入您的选择:"
    value = input(content)
    if value == "1":
        query_balance()
        main_menu()
    elif value == "2":
        deposit()
        main_menu()
    elif value == "3":
        withdraw()
        main_menu()
    elif value == "4":
        print("欢迎下次光临!")
    else:
        print("输入错误, 请重新输入!")
        main_menu()


if __name__ == '__main__':
    main_menu()