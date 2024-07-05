# 多态
class User(object):
    def __init__(self, name):
        self.name = name

    def printUser(self):
        print('Hello !' + self.name)


class UserVip(User):

    # 用双下划线声明私有属性, py 的所有属性都是公共属性, 靠人为避免
    def __init__(self, name, age):
        super().__init__(name)
        self.__name = name
        self.__age = age

    def __pri_md__(self, other):
        print("我是私有方法")

    def printUser(self):
        print('Hello ! 尊敬的Vip用户：' + self.name)


class UserGeneral(User):
    def printUser(self):
        print('Hello ! 尊敬的用户：' + self.name)


def printUserInfo(user):
    user.printUser()


if __name__ == '__main__':
    userVip = UserVip('两点水')
    printUserInfo(userVip)
    userGeneral = UserGeneral('水水水')
    printUserInfo(userGeneral)
