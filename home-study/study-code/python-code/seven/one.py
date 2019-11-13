from enum import Enum


# 定义枚举,枚举的表示全部用大写表示，python中枚举是一个类
class VIP(Enum):
    YELLOW = 1
    RED = 2
    BLACK = 3
    GOLDEN = 4


QQ_vip = VIP
print(QQ_vip.yellow)

#如果没有枚举类，我们怎么定义枚举
#模块中直接定义变量（最差的方式）
#yellow = 1
#red =2
#black = 3
#用字典的方式,这种有数据标签
#{'yellow':1,'red':2,'black':2}
#封装类
# class QQ_VIP():
#     yellow = 1
#     red = 2
#     black =3
#这三种方式的缺陷
    #1可以修改值，类型数据是不能轻易修改的
    #2不能检查重复的的值