# 统计出序列中元素的出现频度
from random import randint

data = [randint(0, 20) for i in range(30)]  # 在0-20之前随机生成30个元素
c = dict.fromkeys(data, 0)

for x in data:
    c[x] += 1

res = {k: v for k, v in c.items() if v >= 2}  # 出现频次大于2
res_tuple = zip(res.values(), res.keys())
print(c)
print(res)
print(sorted(list(res_tuple), reverse=True)[0:3])  # 通过sorted +list切片实现取得出现频次最高的三个

# collection对象统计出序列中元素的出现频度
from collections import Counter

c2 = Counter(data)
print(c2.most_common(3))  # 频次最高的三个
