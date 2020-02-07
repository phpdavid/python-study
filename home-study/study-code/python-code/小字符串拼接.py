s1 = 'abcdefg'
s2 = 'hijklmn'
# 拼接项很少的情况下使用"+",拼接项很多的情况下使用join()方法
s3 = '.'.join([s1, s2])  # ''.join['aaa','bbb','ccc',],join前面是分隔符，''表示不用分隔符拼接join接受列表参数
# print(s3)
s4 = ['adb', 111, 222, 'dcd']  # 列表中含有整数，直接只用join()会报错，要把数字转成字符串
# 方法一使用列表解析
s5 = ''.join([str(x) for x in s4])  # 会生成一个临时列表，列表很长时，是很大一个开销
# print(s5)
# 方法二使用生成器表达式（推荐）
s6 = ''.join((str(x) for x in s4))
print(s6)
