# 学生类
class Student():
    #类变量和类的具体属性无关
    name = ''
    age = 0

    def __init__(self, name, age):
        # 初始化对象的属性
        self.name = name #实例变量
        self.age = age

    def speak(self):
        print("my name is " + name + "i am " + str(age) + " years old")

# def speak(self):
#     print("my name is " + name + "i am " + str(age) + "years old")

# class Printer():
#     def print_file(self):  # 这里必须要加self
#         print('name:' + self.name)
#         print('age:' + str(self.age))

# student = Student()  # 示例中在一个文件，正式环境中不要在一个文件中又定义类，又实例化，调用
# student.print_file()
