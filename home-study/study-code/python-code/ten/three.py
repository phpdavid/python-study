# 查询出现频率最高的5个单词
from collections import Counter
import re

txt = open('test').read()
res = re.split('\W+', txt)
counter = Counter(res)
print(counter.most_common(5))
