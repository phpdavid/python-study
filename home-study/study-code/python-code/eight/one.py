def add(x, y):
    return x + y


add(1, 2)  # 普通函数的调用
# 把add函数用匿名函数实现，也叫作lambda表达式
f = lambda x, y: x + y  # 匿名函数的关键字，不是所有的函数的代码块都可以放到匿名函数，
# 只能是表达式，不能写代码块，不需要return去返回结构，自动返回结果，
print(f(1, 2))  # 调用匿名函数，先复制给一个变量，再调用变量

a = 0
b = 0

c = lambda a, b: a if a > b else b
print(c(3, 2))
