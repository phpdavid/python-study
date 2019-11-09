from one import Student

student = Student('david', 12)

# student.speak('david',12)
# print(student.__dict__) #打印出类包含的元素
# print(Student.__dict__)
student.speak()
# Student.plus_count()#调用类方法
# Student.plus_count()
# Student.plus_count()
student.make_wood(1, 2)  # 对象调用
Student.make_wood(3, 4)  # 类调用
