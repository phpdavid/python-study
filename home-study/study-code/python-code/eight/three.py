from functools import reduce

list_x = [1, 3, 4, 5, 65, 6]
# reduce 连续计算，连续的调用lambda
r = reduce(lambda x, y: x + y, list_x, 10)  # 初始值10
print(r)
# 大数据map/reduce 编程模型，映射/规约，并行计算，python函数是编程主要体现在map/reduce
# filter()  # 过滤

list_a = [9, 0, 9, 0, 9, 0]
# r = filter(lambda x: True if x == 9 else False, list_a)  # filter要求lambda表达式的返回结果为True或False
r = filter(lambda x: True if x == 9 else False, list_a)#简化
print(list(r))

