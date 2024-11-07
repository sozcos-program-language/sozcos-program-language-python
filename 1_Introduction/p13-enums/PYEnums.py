# 定义一个枚举类
from enum import Enum, unique

# 生命一个名为 sex 的枚举, 其中有 men , woman 2个属性
Sex = Enum('sex', ('man', 'woman'))

for name, m in Sex.__members__.items():
    print(name, m, m.value)

# 枚举成员引用
print(Sex.man)


# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'
