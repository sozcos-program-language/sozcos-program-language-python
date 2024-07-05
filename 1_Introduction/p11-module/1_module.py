# 导入模块
import math
import sys
# 直接导入模块的类和方法: from modname import name1[, name2[, ... nameN]]
from sys import version

print(math.pi)
print(version)


if __name__ == '__main__':
    print("is main module")
