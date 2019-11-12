from enum import Enum


# 定义枚举,枚举的表示全部用大写表示
class VIP(Enum):
    YELLOW = 1
    RED = 2
    BLACK = 3
    GOLDEN = 4


QQ_vip = VIP
print(QQ_vip.yellow)
