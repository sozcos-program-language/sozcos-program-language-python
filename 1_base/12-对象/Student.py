class Student:

    # init 函数就是对象的构造器
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):
        return self.age <= other.age

    __name__ = "Student"