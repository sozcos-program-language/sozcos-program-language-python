# 声明一个对象
class ClassA():
    v1 = '我是一个对象'

    # 类方法不需要用 @classmethod 来声明, cls 改成 self 或者其他字母都行 只不过 cls 和 self 都是编程习惯, self 是所有类方法位于首位、默认的特殊参数。
    def m1(self):
        print(self.v1)


class_a = ClassA()
class_a.m1()


# 示例对象的变量以及方法都可以被重写和覆盖

def new_fun(self):
    print("我是一个新函数")


ClassA.v1 = '我是一个新变量'
ClassA.m1 = new_fun

class_a.m1()
print(class_a.v1)

# 但是类方法不能改变
class_a.m1 = new_fun
class_a.m1()
