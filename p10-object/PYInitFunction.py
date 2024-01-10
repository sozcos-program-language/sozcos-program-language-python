class Person(object):

    # 构造参数
    def __init__(self, v1):
        print("__init__ success")
        print(v1)

    # 析构函数, 示例被销毁的时候调用
    def __del__(self):
        print("__del__ success")


person = Person("我是第二个参数")
del person
