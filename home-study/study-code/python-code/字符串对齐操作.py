# 左对齐，右对齐，居中
str = {'name': 'david', 'age': 19, 'gender': 'male', 'role': 'student'}
# 方法一，ljust(10,'=') rjust(10,'-') center(10,'-') 左对齐，右对齐，居中，第一个参数是填充的个数，
# 第二个是填充的字符(可选参数，默认是空白)
# for x, y in str.items():
# print(x.ljust(6), ':', y)
# 方法二 format()
# print(format(x,'<6'),':',y)#左对齐
# print(x,':',format(y,'>16'))#右对齐
# print(x,':',format(y,'^16'))#居中对齐
w = max(map(len, str.keys()))
for k, v in str.items():
    print(k.ljust(w), ':', v)
