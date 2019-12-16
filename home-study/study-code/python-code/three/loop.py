"""
循环
"""

counter = 0
# list 列表类型
condition_list = ['apple_list', 'banana_list', 'orange_list', 'grape_list']
# tuple 元祖类型
condition_tuple = ('apple_tuple', 'banana_tuple', 'orange_tuple', 'grape_tuple')
# set 集合类型
condition_set = {'apple_set', 'apple_set', 'orange_set', 'grape_set'}
# dict 字典类型
condition_dict = {'a': 'apple_dict', 'b': 'banana_dict', 'o': 'orange_dict', 'g': 'grape_dict'}
# 多维
condition_all = [['apple_list', 'banana_list', 'orange_list', 'grape_list'],
                 ('apple_tuple', 'banana_tuple', 'orange_tuple', 'grape_tuple'),
                 {'apple_set', 'apple_set', 'orange_set', 'grape_set'},
                 {'a': 'apple_dict', 'b': 'banana_dict', 'o': 'orange_dict', 'g': 'grape_dict'}
                 ]
while counter <= 10:
    counter += 1
    if counter == 5:
        print(55)
    print(counter)
else:
    print('its over')

# for x in condition_all:  # 遍历多维数组
#     for y in x:
#         print(y)
# else:  # 虽然python有else这个语法，但是不常用
#     print('game over')

for x in condition_list:
    # if x == 'orange_list':
    if 'orange_list' in x:
        # break  # 强行终止循环，跳出当前的循环 orange_list 和orange_list 后面的元素不会打印
        continue  # 跳过当前的元素 orange_list 这个元素不会打印
    print(x)
else:  # 执行break强行终止,else的代码段将不会执行
    print('game over')

# for x in range(0, 10, 2):  # 对应for(i=1;i<=10;i++) range：生成一个序列(第一个参数其市值，第二个参数是范围，相当于小于，第三个可选参数是步长)
for x in range(10, 2, -2):  # 递减排列，第一个参数大于第二个参数，第三个参数为负数
    # if x % 2 == 1:
    print(x, end='|')  # end='|'是一行打印出来
else:
    print('\n')
# 打印位置长度的列表
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for x in range(0, len(a), 2):  # len()获取列表的长度作为range的第二个参数
    print(x, end="|")

b = a[0:len(a):2]  # 利用列表的切片去除元素，第一个参数是起始位置，第二个是切片的长度，第三个是步长
print(b)

# 遍历字典,相当于PHP foreach()循环
for a in condition_dict:
    print(a)  # 打印key
    print(condition_dict[a])  # 打印value

for key in condition_dict.keys():  # keys()打印key
    print(key)

for value in condition_dict.values():  # 使用value()打印value
    print(value)
# 使用items()遍历key,value
for kv in condition_dict.items():  # 遍历字典项
    print(kv)
for key, value in condition_dict.items():
    print(key + ':' + value)
