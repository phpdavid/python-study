import time


def f1():
    print('f1')


def f2():
    print('f2')


def f3():
    print('f3')


# 给每个函数添加打印时间的功能，不能违反封闭原则：对修改是封闭的，对扩展是开放的
# 定义一个打印时间的函数，调用原有的函数
def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
print_current_time(f3)


# 用装饰器模式改造
def decorator(func):
    def wrapper(*args, **kwargs):  # *args为执行函数添加参数，可变参数，任意几个参数,
        # 没有参数，执行函数不能带参数
        print(time.time())
        func(*args, **kwargs)

    return wrapper


@decorator  # python语法糖
def f4():
    print('f4')


f4()


@decorator
def f5(x, y, z):
    print(x + y + z)


f5(1, 2, 3)


@decorator
def f6(x, y):
    print(x + y)


f6(1, 2)


@decorator
def f7(x, y, **kw):  # **kw关键字参数，可以任意命名,打印的结果是字典
    print(x + y)
    print(kw)


f7(1, 2, a=2, b=3, h=9, aa=2, ba=3, ha=9)#加上**KW关键字参数， a=2, b=3, h=9....可以随意加多少参数

# f = decorator(f4)#传统调用装饰器
# f()
