# 学生类
class Student():
    # 类变量和类的具体属性无关
    name = 'xiaoming'  # 姓名，年龄是个体的属性，不是群体的属性，不建议
    age = 10
    # 学生总数
    sum = 0

    def __init__(self, name, age):
        # 初始化对象的属性
        self.name = name  # 实例变量
        self.age = age
        # self.__class__.sum+=1 #操作类变量加一操作
        # print(self.__class__.sum)

    # 定义类方法
    @classmethod  # 装饰器
    def plus_count(cls):  # cls代表类本身， 主要用于操作类变量的操作
        cls.sum += 1
        print(cls.sum)
        # print(self.name) #不能请求对象的变量

    # 定义实例方法
    def speak(self):  # self代表对象本身
        self.eat()
        print("my 类 name is " + __class__.name + " i am " + str(__class__.age) + " years old")
        print("my 对象 name is " + self.name + " i am " + str(self.age) + " years old")

    def eat(self):
        print('i like beef')

    # 定义静态方法
    @staticmethod
    def make_wood(x, y):  # 不需要cls,self这些关键字
        print("this is a static method")
        # print(self.name)#不能请求对象的变量
# class Printer():
#     def print_file(self):  # 这里必须要加self
#         print('name:' + self.name)
#         print('age:' + str(self.age))

# student = Student()  # 示例中在一个文件，正式环境中不要在一个文件中又定义类，又实例化，调用
# student.print_file()
