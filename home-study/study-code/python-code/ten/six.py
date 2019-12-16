# 字典保持有序,先进先出，默认是后进先出
from collections import OrderedDict

d = OrderedDict()
d['bob'] = (1, 22)
d['jim'] = (2, 65)
d['david'] = (3, 77)

for k in d:
    print(k)
