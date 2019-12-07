# 根据字典中值的大小，对字典中的项进行排序

# 随机生成一份字典
from random import randint

data = {x: randint(60, 100) for x in "zxsefa"}

a = data.values()
b = data.keys()
res = zip(a, b)  # 通过zip函数转换为列表，用sorted进行比较

print(list(sorted(res, reverse=True)))

res_item = sorted(data.items(), key=lambda x: x[1], reverse=True)  # items()函数配合lamda
print(res_item)
