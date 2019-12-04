from random import randint

# 遍历筛选大于10的值
from timeit import timeit

data = [1, 2, 3, 45, 56, 67, 7, 8, 5]

res = []
for i in data:
    if i >= 10:
        res.append(i)

# print(res)
data = [randint(-10, 10) for i in range(10)]  # 随机生成list
res = filter(lambda x: x >= 0, data)  # filter+lambda实现过滤
# print(list(res))
res = [x for x in data if x >= 0]  # 列表推导式，实现过滤,列表解析的速度更快，推荐使用
# print(res)
d = {x: randint(60, 100) for x in range(1, 21)}  # 随机生成disc
# print(d)
res = {k: v for k, v in d.items() if v > 90}
print(res)
