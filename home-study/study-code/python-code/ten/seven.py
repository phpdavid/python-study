# 模拟竞赛系统,按照名次打印
from random import randint
from time import time
from collections import OrderedDict
from pip._vendor.distlib.compat import raw_input

d = OrderedDict()
players = list('ABCDEFGH')
pos = len(players)-1
start = time()

for i in range(len(players)):
    raw_input()

    p = players.pop(randint(0, pos - i))
    end = time()
    d[p] = (i+1,end - start)
for k,v in d.items():
    print(k,v)


