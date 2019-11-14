from enum import Enum
from enum import IntEnum, unique  # 强制数字类型,unique是一个装饰器强制唯一性


# 定义枚举,枚举的表示全部用大写表示，python中枚举是一个类
@unique  # 开启唯一性
class VIP(Enum):
    YELLOW = 1  # 大写表示常量
    YELLOW1 = 1  # 默认情况下，遍历别名不会被打印出来
    RED = 2  # 名字不能相同，当值相同的时候，第二个名字，会被当做第一个名字的别名
    BLACK = 3
    GOLDEN = 4


QQ_vip = VIP
# for v in QQ_vip.__members__.items():  # 连同别名一起打印，返回元祖
#     print(v)
# QQ_vip.RED = 6#枚举不可以被更改
# print(QQ_vip.YELLOW)#这样不能打印YELLOW的值，打印是枚举的类型
# print(QQ_vip.YELLOW.value)  # 打印YELLOW的值
# print(QQ_vip.YELLOW.name)  # 打印YELLOW的名称
# print(VIP.RED)#打印枚举的类型
# 枚举的比较
r = QQ_vip.RED.value < QQ_vip.BLACK.value  # 枚举之间是不能做大小比较的，但是可以做等值比较，身份is比较，值可以比较

# print(r)
# for v in QQ_vip:  # 遍历枚举
#     print(v)


a = 1
r = VIP(a)
print(r)
