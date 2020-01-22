import random
import time

## 循环+判断


data = [random.randint(-10, 10) for _ in range(10)]
# a = []
# for _ in data:
#     if _ >= 0:
#         a.append(_)
# print(a)
## list+fileter+lambda函数

# a = list(filter(lambda x: x >= 0, data))
# print(a)
##推导表达式

# a = [_ for _ in data if _ >= 0]
# print(a)
##字典的遍历+判断查找
dict_data = {_: random.randint(60, 100) for _ in range(1, 100)}
# print(dict_data)
#
# t0 = time.process_time()
# a = {}
# for k, v in dict_data.items():
#     if v >= 80:
#         a[k] = v
# t1 = time.process_time()
# print(t1 - t0)
# print(a)
a = {k: v for k, v in dict_data.items() if v >= 80}
print(a)
