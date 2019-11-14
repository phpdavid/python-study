a = 50  # 全局变量


def curve_pro():  # 闭包=函数+环境变量
    a = 25  # 环境变量

    def curve(x):  # 被定义，并没有被执行，返回到我们的模块中，
        # 当我们在模块中调用curve的时候，内部a的值，不会去模块中的变量，而是取的定义的时候的环境变量
        # 这就是闭包
        return a * x * x

    return curve  # 函数可以被返回


a = 100  # 模块中的变量
f = curve_pro()

print(f(23))  # 打印闭包
