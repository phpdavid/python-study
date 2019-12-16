# 定义人的类
class Human():
    # __head = 1
    # __leg = 2
    # __arm = 2
    sum = 0

    def __init__(self, name, age):
        # 初始化对象的属性
        self.name = name  # 实例变量
        self.age = age
        self.__score = 0
        self.__class__.sum += 1  # 操作类变量加一操作
        print(self.__class__.sum)

    def say(self):
        print(self.name + str(self.age))
