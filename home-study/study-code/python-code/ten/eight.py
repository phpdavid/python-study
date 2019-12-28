# 竞猜小程序
from random import randint
from collections import deque
import pickle

from pip._vendor.distlib.compat import raw_input

N = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less-than N' % k)
    else:
        print('%s is greater-than N' % N)
        return False


while True:
    line = raw_input('please input ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h':
        print(history)
