"""
循环练习:
公司总共有 1w 元, 有 20名员工, 随机给出员工绩效分, 绩效分小于5分则不发工资, 直到工资发完
"""

import random

total_price = 10000

for emp in range(1, 21):
    performance = random.randint(1, 5)
    if performance < 5:
        print(f"员工{emp}的绩效分{performance}, 不发工资")
        continue

    if total_price >= 1000:
        total_price -= 1000
        print(f"员工{emp}发了1000元工资, 剩余{total_price}元")
    else:
        print(f"剩余工资{total_price}")
        break
