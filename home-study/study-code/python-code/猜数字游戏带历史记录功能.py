from random import randint
from collections import deque

# 猜大小游戏
# 先设置一个随机数
N = randint(0, 100)
# 历史记录，用大小为5的队列装
history = deque([], 5)


def guess(k):
    if k == N:
        print('right')
    elif k < N:
        print('小了')
    else:
        print('大了')
    return False


while True:
    line = input("please input a number between 0 and 100:")
    if line.isdigit():
        k = int(line)
        # 装入队列
        history.append(k)
        # 输入的值与设置的值比较
        if guess(k):
            break
    if line == 'history' or line == 'h!':
        print(list(history))
