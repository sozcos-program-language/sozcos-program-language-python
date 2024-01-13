class Man(object):
    def __new__(cls, *args, **kwargs):
        print('调用了new函数')
        return super().__new__(cls)  # 如果没有返回实例对象,那么则会接受到一个 none 值

    def __init__(self, name):
        print('调用了init函数', 'name={}'.format(name))


# 查看类的魔法方法
print(Man('param'))
