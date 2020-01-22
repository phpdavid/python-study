from collections import Counter
import re

# from random import randint
# data = [randint(0,10) for _ in range(20)]
# # print(data)
# data = Counter(data)
# print(data.most_common(5))
with open('../../pycharm快捷方式.txt', encoding="utf-8") as f:
    wordStr = f.read()
    # print(wordStr)
    wordList = re.split('\W+',wordStr)
    # print(wordList)
    wordCount = Counter(wordList)
    print(wordCount.most_common(3))