# 正则表达式
import re  # 引入正则表达式模块

# a = "c|c++|java|php|php|go|php"
## 通过python内置变量查找字符串，优先使用
# print(a.index("python") > 1)
# print('python' in a)
## 正则表达式查找普通字符
# result = re.findall('python', a)
# if len(result) > 0:
#     print('a 中包含python', result)
# else:
#     print('a 中不包含python')

# ## 正则表达式，元字符
# b = "adg2kj3n4n5bn6b3n3nb5b43n2n7"
# r = re.findall('\d', b)  # 概括字符集，匹配所有的数字
# r = re.findall('\D', b)  # 概括字符集，匹配所有非数字
# print(r[0:2]) ##切割字符串

##字符集

s = 'abc,agc,afc,acc,aec'

# r = re.findall('a[cf]c', s)  ##带有c或者f的单词[cf]中c和f是或的关系
# r = re.findall('a[^cf]c', s)  ##取反，没有c或者f的单词
# r = re.findall('a[c-f]c', s)  ##匹配c-f的单词
# print(r)

##概括字符集
# b = "adg2kj3n4n5bn6b\n\t\r3n3nb5b4&*@3n2n7_"
#
# # re.findall('\d', b)  # 概括字符集，匹配所有的数字 \d = [0-9]
# # re.findall('\D', b)  # 概括字符集，匹配所有非数字 \D = [^0-9]
# # r = re.findall('\w', b)  # 概括字符集，匹配所有数字和非字母和下划线[A-Za-z0-9_]
# # r = re.findall('\W', b)  # 概括字符集，匹配所有非数字，非字母和非下划线[^A-Za-z0-9_]
# # r = re.findall('\s', b)  # 概括字符集，空格，回车，制表符等空白字符，不包括&
# r = re.findall('\S', b)  # 概括字符集,非空白字符
# r = re.findall('.', b)  # 概括字符集,除换行符\n之外所有字符
# print(r)

##数量词
# b = "adg2kj3 n4n5bn6b\n\t\r3n3nb5pythonb4&*@3n2javan7_php"

# r = re.findall('[a-z]{3,6}', b)  # 大括号表示重复中括号中的匹配，3,6表示匹配字符串的位数，最小3位，最大6位
# r = re.findall('[a-z]{3,6}?', b)  # 非贪婪模式，大括号表示重复中括号中的匹配,匹配到就结束
# print(r)

# b = 'pytho0python1pythonn2'
# # r = re.findall('python*', b)  # “*”匹配前面的字符0次或者n次
# # r = re.findall('python+', b)  # “+”匹配前面的字符1次或者n次
# r = re.findall('python?', b)  # “+”匹配前面的字符0次或者1次 ##pythonn这种情况，也会匹配到，后面一个n会被删掉，因为只能出现一次
# ### ?的使用场景{3,6}?在范围之后出现表示非贪婪，在字符后出现表示重复
# print(r)

# b = '88560200058'

# r = re.findall('^\d{4,8}$', b)  # 边界匹配^开始$结束,限定字符串的边界，^表示从头开始匹配，$表示从末位开始匹配
# print(r)

# b = 'pythonpythonpythonpythonpythonjs'
# r = re.findall('(python){3}', b)##()表示组，re.findall('(python){3}(js){1}', b),可以有多个组
# print(r)

language = 'PythonC#PHP\nJAVA'
r = re.findall('php.{1}', language, re.I | re.S)  ##第三个参数是模式参数，re.I匹配模式忽略大小写,re.S让“.”包括换行符，可以接受多种模式
print(r)
