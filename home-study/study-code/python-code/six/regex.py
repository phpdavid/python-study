import re

s = '1qq123jkl833k3dkdk66pd0PHP'


# 定义正则表达式函数
def convert(value):
    # #找到指定的字符串，返回前后拼接下划线
    # mathod = value.group()
    # return "__" + mathod + "__"
    mathod = value.group()
    if int(mathod) > 6:
        mathod = '0'
    elif int(mathod) < 6:
        mathod = '9'
    else:
        mathod = 'w3'

    return mathod


# r = re.sub('\d', convert, s)
# r = re.sub('PHP', convert, s)#找到指定的字符串，返回前后拼接下划线
# r = re.findall('\D', s, re.I) #正则查找查找
# print(r)
#
# r1 = re.match('\d', s)  # 返回none,特征从字符串的首字母匹配，如果没有匹配到数字，返回none
# r2 = re.search('\d', s)  # 特征，搜索整个字符串，一旦找到结果，马上返回结果
# print(r1.group())  # 利用group方法提取匹配到的结果
# print(r2.group())

a = 'life is shot i use python , i love python'

r3 = re.search('life(.*)python', a)  # 普通字符可以当做一个字符串的定界符，life是开始，python时是结尾,用小括号分组
print(r3.group(1))  # group的意义在于获取分组的匹配，默认是0，group(0)是一个特殊的表达方法，永远返回的都是完整的字符串,取值从1开始
print(re.findall('life(.*)python', a))  # findall直接返回匹配到的结果
r4 = re.search('life(.*)python(.*)python', a)  # 多个分组
print(r4.group(0, 1, 2))  # 返回多个分组
print(r4.groups())  # 返回匹配到的多个分组
