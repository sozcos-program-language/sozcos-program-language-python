# 继承
class Man(object):
    def __init__(self):
        print("Man is init")


class Person(object):
    def __init__(self):
        print("I am a person")


class Student(Person, Man):
    def __init__(self):
        super().__init__()
        print("I am a student")


s1 = Student()
