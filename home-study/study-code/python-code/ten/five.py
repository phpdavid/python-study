from functools import reduce
from random import randint, sample

# 公共键
names = ['david', 'tom', 'zhou', 'dayu', 'moto', 'jim']  # 定义一组球员名字
s1 = {x: randint(1, 3) for x in sample(names, randint(3, 6))}  # 为球员随机生成每场得分
s2 = {x: randint(1, 3) for x in sample(names, randint(3, 6))}  # 为球员随机生成每场得分
s3 = {x: randint(1, 3) for x in sample(names, randint(3, 6))}  # 为球员随机生成每场得分
# sample随机取样，randint指定范围生成随机整数

# 找出每场都有进球的球员
# 1遍历+判断的方式
res = []
for k in s1:  # 遍历其中一组进球数据的键
    if k in s2 and k in s3:  # 到另外两组数据中对比，两组都存在就保存
        res.append(k)
# print(res)

# 2利用集合（set）的交集操作
result = set(s1.keys() & s2.keys() & s3.keys())
# print(result)

# 3 map +reduce取交集
# arg = map(dict.keys, [s1, s2, s3])
# res3 = reduce(lambda x, y: x & y, arg)
res3 = reduce(lambda x, y: x & y, map(dict.keys, [s1, s2, s3]))
print(res3)
