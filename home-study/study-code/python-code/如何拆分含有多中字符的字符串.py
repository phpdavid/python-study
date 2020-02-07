# 根据分隔符拆分不同的字段
# 方案一，循环迭代，拆分列表分割
def mySplit(s, ds):
    data = [s]
    # print(data)
    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)), data))
        data = t
    return [x for x in data if x]


s = 'ab;cd|efg|hi,gkl|mn\topq;rst,uvw\tsyz'

# res = mySplit(s, ';|,\t')
# print(res)
# 方案二，使用re.split(),一次性分割字符串[推荐]
import re
res = re.split(r'[,;\t|]+',s)
print(res)