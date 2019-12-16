# 使用类枚举的方式（python中没有枚举类型）为元祖每个元素命名，提高程序可读性
# 在python中没有真正的枚举类型，我们可以定义一些常量代替

Student = ('david', 19, 'male')
# # 通过下标读取值，可读性很差，时间久了，不知道是什么了
# # name
# Student[0]
# # age
# Student[1]
# # gender
# Student[2]
#
# # 定义常量
# # NAME = 0
# # AGE = 1
# # GENDER = 2
# NAME, AGE, GENDER = range(3)
# Student[NAME]
# Student[AGE]
# Student[GENDER]
# print(Student[NAME])
# 2通过collection中的nametuple定义
from collections import namedtuple

Student = namedtuple('Human', ['name', 'age', 'gender'])
s = Student('david', 16, 'female')
print(s.name)  # 以类，对象的形式访问元祖
