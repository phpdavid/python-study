import re

language = 'PythonC#JavaPHP'


# 正则替换
# r = re.sub('PHP', 'GO', language)#直接出入替换的字符串
def convert(value):
    print(value)  # value是个对象
    mathod = value.group()  # 通过对象group方法拿到匹配到的值
    return "__" + mathod + "__"  # 返回加工后的值


r = re.sub('PHP', convert, language)  # 传入一个函数，动态的替换
print(r)
# # 字符串函数替换
# d = language.replace('Java', 'JS')
# # 字符串替换有限使用内置函数，解决不了的，在使用正则表达式，内置函数解决不了的，正则表达式都能解决
# # 正则替换的强大之处在于可以出入一个函数
# print(d)
