# 列表推导式
# 集合set也可以被推导
# 字典也可以被推导
# 元祖可以被推导
a = [1, 22, 3, 4, 56]  # 列表
b = [i ** 2 for i in a if i >= 3]  # if 可选筛选条件
print(b)

c = {1, 2, 8, 40, 692}  # 集合
d = {i * 3 for i in c}  # if 可选筛选条件
print(d)

e = [1, 2, 8, 40, 692]  # 元祖
f = [i * 5 for i in e]  # if 可选筛选条件
print(f)


def cut_word(i):
    return i[0:-2]


g = {"a": "apple", "b": "banana", "c": "cherry", "d": "durian"}  # 字典
h = [cut_word(i) for i in g.values()]  # if 可选筛选条件
print(h)
