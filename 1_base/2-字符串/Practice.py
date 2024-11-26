# 字符串格式化练习
"""股价计算小程序
定义如下变量:
name，公司名
stock_price，当前股价
stock_code，股票代码
stock_price_daily_growth_factor，股票每日增长系数，浮点数类型，比如1.2
growth_days，增长天数
计算，经过growth days天的增长后，股价达到了多少钱使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数"""

name = "腾讯控股"
stock_price = 7.5
stock_code = "00700"
stock_price_daily_growth_factor = 1.2
growth_days = 5

print(f"经过{growth_days}天的增长, 股价达到了%.2f元。" % (
            stock_price + (stock_price * stock_price_daily_growth_factor * growth_days)))
