def calculate_break_even_months(daily_profit, total_monthly_cost):
    # 每月盈利
    monthly_profit = daily_profit * 30  # 假设每月30天

    # 计算回本周期
    months_to_break_even = -(-total_monthly_cost // (monthly_profit - total_monthly_cost))  # 使用负数整除来实现向上取整

    return months_to_break_even

def main():
    # 输入每日盈利
    daily_profit = float(input("请输入每日盈利（元）："))

    # 初始化每月成本总额
    total_monthly_cost = 0.0

    # 输入成本明细
    while True:
        cost_item = input("请输入成本明细（例如：手机费用，卡月租费用，宽带费用，电费等），输入'完成'结束：")
        if cost_item == "完成":
            break
        try:
            cost = float(cost_item)
            total_monthly_cost += cost
        except ValueError:
            print("输入无效，请输入一个数值。")

    # 计算回本周期
    months_to_break_even = calculate_break_even_months(daily_profit, total_monthly_cost)

    # 输出结果
    print(f"每月成本总额为：{total_monthly_cost} 元")
    print(f"回本周期为：{months_to_break_even} 个月")

if __name__ == "__main__":
    main()