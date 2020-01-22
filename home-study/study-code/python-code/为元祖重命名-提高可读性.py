##用类似枚举的方式
# student = ('sam', 18, 'male', '13800138000')
# NAME, AGE, GENDER, PHONE = range(4)
# print(student[NAME],student[AGE],student[GENDER],student[PHONE])
# student = ('sam', 18, 'male', '13800138000')
## namedtuple
from collections import namedtuple

Student = namedtuple('xiaoming', ['name', 'age', 'gender', 'phone'])
student = Student('sam', 88, 'woman', 123456789)
print(student.name, student.age, student.gender, student.phone)
