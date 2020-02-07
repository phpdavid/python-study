# 方法一，去掉字符串前后的字符，空白

str = '==  ss dd++ee--oo++  --'
str.lstrip()  # 去掉左边字符
str.rstrip()  # 去掉右边字符
# print(str.strip('=-'))  # 去掉两边字符

# 方法二，切片+拼接的方式
# print(str[0:2]+str[4:6]+str[8:12])

# 方法三，replace方法
# print((((str.replace('=','')).replace('+','')).replace(' ','')).replace('-',''))
# 方法四，正则替换
import re

# print(re.sub('[\W]','',str))
# 方法五，str.maketrans方法
str_map = str.maketrans(' ', ' ')  # 创建映射的字典，就是替换和原始字符的对应
# print(str.translate(str_map))#映射字典作为translate的参数
