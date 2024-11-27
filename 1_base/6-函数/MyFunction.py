"""
定义一个函数, 调用函数的时候返回一个字符串"Hello, World!"
"""

def say_hello():
    print("Hello, World!")


"""
定义一个函数, 接受一个number类型的的参数, 这个参数是体温, 高于 37度的时候输出需要隔离, 反之输出正常
"""
def check_temperature(body_temperature):
    if body_temperature < 36.5:
        return "正常"
    elif body_temperature < 37.5:
        return "轻度发冷"

if __name__ == '__main__':
    print(check_temperature(37))
