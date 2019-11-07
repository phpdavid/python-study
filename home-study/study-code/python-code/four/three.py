# a = 1
# b = 2
# c = 3
# a, b, c = 1, 2, 3  # 简洁的写法
# d = 1, 2, 3  # 元祖类型通 d = [1,2,3]
# print(type(d))
# a, b, c = d  # 序列解包,这里要注意元素的数量要相等
# print(a, b, c)


def add_test(a, b):
    d = a + b
    return d


e = add_test(a=4, b=6)
print(e)
