# 求列表每个元素的平方，返回这个列表
list_x = [4, 7, 3, 4]
list_y = [3, 4, 5, 6, 7]


def sque(x):
    return x * x


# for i in range(len(list_x)):#遍历的方式
#     list_x[i] = sque(list_x[i])
#
# print(list_x)
# r = map(sque,list_x)
r = map(lambda x, y: x * x + y, list_x, list_y)  # lambda+map配合
print(list(r))
