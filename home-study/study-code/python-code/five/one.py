# 学生类
from three import Human  # 导入模块


class Student(Human):  # 继承父类
    # 类变量和类的具体属性无关
    # 私有函数
    __name = 'xiaoming'  # 姓名，年龄是个体的属性，不是群体的属性，不建议
    # 共有函数
    name = 'david'
    __age = 10
    # 学生总数
    __sum = 0

    def __init__(self, school, name, age):
        # 初始化对象的属性
        # self.__name = name  # 实例变量
        # self.__age = age
        self.__score = 0
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)  # super关键字调用父类的构造函数
        self.school = school
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
        super(Student, self).say()  # 继承父类的方法
        self.__eat()
        # print("my 类 name is " + __class__.__name + " i am " + str(__class__.__age) + " years old")
        print("my 对象 name is " + self.__name + " i am " + str(self.__age) + " years old")
        # print("i have "+ parent.__leg)
        print(self.school)

    def set(self, score):
        if score < 0:
            score = 0
        self.__score = score

    # 私有方法
    def __get(self):
        print(self.__score)

    # 共有方法
    def get(self):
        print(self.__score)

    def __eat(self):
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
