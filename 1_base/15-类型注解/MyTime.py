import time


def accelerate_time(acceleration_factor):
    """
    根据加速因子加速时间。

    参数:
    acceleration_factor (int): 加速因子，例如1, 2, 3, 4, 5
    """
    # 计算实际的时间间隔
    actual_interval = 1.0 / (1 + 0.1 * acceleration_factor)

    # 初始化时间
    start_time = time.time()
    virtual_start_time = start_time

    while True:
        # 获取当前实际时间
        current_time = time.time()
        elapsed_real_time = current_time - start_time

        # 计算虚拟时间
        elapsed_virtual_time = (current_time - virtual_start_time) * (1 + 0.1 * acceleration_factor)

        # 打印正常时间和加速后的时间
        print(f"正常时间: {elapsed_real_time:.2f} 秒 | 加速时间: {elapsed_virtual_time:.2f} 秒")

        # 等待实际的时间间隔
        time.sleep(actual_interval)


# 获取用户输入的加速比例
try:
    acceleration_factor = int(input("请输入加速比例（例如1, 2, 3, 4, 5）："))
    if acceleration_factor < 1:
        print("加速比例必须大于等于1。")
    else:
        accelerate_time(acceleration_factor)
except ValueError:
    print("请输入有效的整数。")
