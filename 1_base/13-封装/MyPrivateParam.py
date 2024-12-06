class Phone:
    __is__5g_enable = true

    def __check_5g(self):
        if self.__is__5g_enable:
            print("5G 开启")
        else:
            print("5G 关闭, 使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
