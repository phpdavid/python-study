from random import randint
from itertools import chain

# 需求求出班上40名学生的语文，数学，英语的总分
# students = ['bob', 'ada', 'joe', 'wan', 'sun', 'li', 'david', 'lucy', 'wow']
# chinese = [randint(60, 100) for _ in range(40)]
# math = [randint(60, 100) for _ in range(40)]
# english = [randint(60, 100) for _ in range(40)]
#
# # 第一种方法，使用检索,但是局限性
# # for x in range(len(chinese)):
# #     all = chinese[x] + math[x] + english[x]
# #     print(all)
# # 这种并行的情况可以使用内置函数ZIP，可以将多个可迭代多想组合起来
# total =[]
# for c,m,e in zip(chinese,math,english):
#     total.append(c+m+e)
# print(total)

# 四个班，每个班的英语成绩存储在一个表，一次迭代每个班，统计全学年成绩高于90分人数
# chain 函数可以把可迭代对象串联起来
c1 = [randint(60, 100) for _ in range(40)]
c2 = [randint(60, 100) for _ in range(38)]
c3 = [randint(60, 100) for _ in range(36)]
c4 = [randint(60, 100) for _ in range(41)]

count = 0
for s in chain(c1, c2, c3, c4):
    if s > 90:
        count += 1
print(count)
