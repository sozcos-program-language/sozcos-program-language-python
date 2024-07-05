# 使用threading声明一个线程
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("线程: {}, @num: {}".format(self.name, i))
            time.sleep(1)


def main():
    print("开启线程")

    # 创建3个线程
    threads = [MyThread() for i in range(3)]
    # 启动线程
    for thread in threads:
        thread.start()

    print("结束创建线程")


if __name__ == '__main__':
    main()