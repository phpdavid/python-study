# 查询出现频率最高的5个单词
from collections import Counter
import re

txt = open('test').read()  # 读取文件
res = re.split('\W+', txt)  # 正则分割
counter = Counter(res)  # counter计数
print(counter.most_common(5))  # 排序
