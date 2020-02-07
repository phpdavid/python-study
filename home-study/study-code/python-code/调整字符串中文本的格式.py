# 把log文件中日期格式YYYY-mm-dd修改为mm/dd/YYYY
import re
#使用正则表达式re.sub做字符串的替换，利用正则表达式的捕获组，捕获每个部分的内容，调整字符串的顺序
log = open('test.log').read()
log1 = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)  # r参数表示原始字符串，用原始字符串替换，修改格式
# 用别名的方式代替分组符号\2/\3/\1
log2 = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<year>/\g<day>',
              log)  # r参数表示原始字符串，用原始字符串替换，修改格式
print(log2)
