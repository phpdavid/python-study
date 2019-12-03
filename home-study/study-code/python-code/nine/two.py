from collections import namedtuple

NAME = 0
AGE = 1
GENDER = 2
# 利用类似常量的方式访问元祖的值，代替元祖的键值
student = ('david', 18, 'male')

student[NAME]
student[AGE]
student[GENDER]

# 利用namedtuple库，生成元祖的键值
student_pro = namedtuple('student_pro', ['name', 'age', 'gender'])
s = student_pro('dawang', 20, 'female')
print(s.name)  # 类，对象的形式，访问元祖
