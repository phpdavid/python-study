from random import randint
from collections import OrderedDict
from time import time

d = OrderedDict()
player = ['bob', 'cc', 'JJ', 'GG']
start = time()
for i in range(4):
    input()
    p = player.pop(randint(0, 3 - i))
    end = time()
    print(i + 1, p, end - start)
    d[p] = (i + 1, end - start)
print('----------')

for k in d:
    print(k)
