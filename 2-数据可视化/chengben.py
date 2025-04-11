import calendar
from datetime import datetime

# 获取当前年月和天数
today = datetime.today()
year = today.year
month = today.month
days_in_month = calendar.monthrange(year, month)[1]


def input_monthly_costs():
    """
    输入本月的成本项，逐项输入，回车结束
    """
    print("📥 请输入本月成本项如：月租，宽带，电费，水费等（每次输入一个金额，按回车结束）：")
    costs = []
    while True:
        value = input("> ")
        if value.strip() == "":
            break
        try:
            cost = float(value)
            costs.append(cost)
        except ValueError:
            print("⚠️ 请输入有效数字")
    return sum(costs)


def input_daily_revenue():
    """
    输入每日收益金额
    """
    while True:
        try:
            revenue = float(input("\n请输入每日盈利金额："))
            return revenue
        except ValueError:
            print("⚠️ 请输入有效数字")


def calc_gross_profit(daily_revenue, monthly_cost, days_in_month):
    """
    计算每日毛利
    """
    daily_cost = monthly_cost / days_in_month
    daily_profit = daily_revenue - daily_cost
    return daily_profit, daily_cost


def print_month_summary(daily_profit, daily_cost, daily_revenue, monthly_cost, days_in_month):
    """
    打印当前月份的汇总
    """
    total_revenue = daily_revenue * days_in_month
    total_profit = daily_profit * days_in_month

    print(f"\n------ {year} 年 {month} 月 汇总 ------")
    print(f"天数：{days_in_month} 天； 总盈利：{total_revenue:.2f} 元； 总成本：{monthly_cost:.2f} 元； 总毛利：{total_profit:.2f} 元")
    print(f"每日成本：{daily_cost:.2f} 元； 每日毛利：{daily_profit:.2f} 元")

    return total_revenue, total_profit


def print_year_summary(monthly_revenue, monthly_cost):
    """
    打印全年汇总（按当前月情况估算）
    """
    total_yearly_revenue = monthly_revenue * 12
    total_yearly_cost = monthly_cost * 12
    yearly_profit = total_yearly_revenue - total_yearly_cost

    print(f"\n------ {year} 全年 汇总 ------")
    print(f"总盈利：{total_yearly_revenue:.2f} 元； 总成本：{total_yearly_cost:.2f} 元； 总毛利：{yearly_profit:.2f} 元")


def print_payback_cycle(monthly_cost, daily_profit, days_in_month):
    """
    输出当前成本和毛利下的回本周期
    """
    print("\n------ 回本周期 ------")
    if daily_profit <= 0:
        print("❌ 每日毛利为负或为 0，无法计算回本周期")
    else:
        days_to_payback = monthly_cost / daily_profit
        months_to_payback = days_to_payback / days_in_month
        print(f"累计回本天数：{days_to_payback:.2f} 天； 累计回本月数：{months_to_payback:.2f} 个月")


def suggest_cost_by_target_days(daily_profit, days_in_month):
    """
    根据目标回本周期（30/60/90天）建议最大月成本
    """
    print("\n------ 建议投入成本（按目标回本周期） ------")
    if daily_profit <= 0:
        print("⚠️ 当前每日毛利为 0 或负值，建议不要投入成本。")
        return

    for days in [30, 60, 90]:
        max_total_cost = daily_profit * days
        suggested_monthly_cost = max_total_cost / days * days_in_month
        print(f"🕒 希望在 {days} 天内回本，建议每月投入不超过：{suggested_monthly_cost:.2f} 元/月")


def main():
    monthly_cost = input_monthly_costs()
    daily_revenue = input_daily_revenue()

    daily_profit, daily_cost = calc_gross_profit(daily_revenue, monthly_cost, days_in_month)

    total_revenue, total_profit = print_month_summary(
        daily_profit, daily_cost, daily_revenue, monthly_cost, days_in_month
    )

    print_year_summary(total_revenue, monthly_cost)
    print_payback_cycle(monthly_cost, daily_profit, days_in_month)
    suggest_cost_by_target_days(daily_profit, days_in_month)


if __name__ == "__main__":
    main()
