from random import randint
from random import sample
from functools import reduce

# data = sample('acdidhang',randint(3,6))#随机取样
# print(data)
s1 = {x: randint(1, 4) for x in sample('abidndx', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abidndx', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abidndx', randint(3, 6))}
s4 = {x: randint(1, 4) for x in sample('abidndx', randint(3, 6))}

##方法一
# sKey = s1.keys() & s2.keys() & s3.keys() & s4.keys()
# print(sKey)
##方法二
a = map(dict.keys, [s1, s2, s3, s4])
b = reduce(lambda x, y: x & y, a)
print(b)
