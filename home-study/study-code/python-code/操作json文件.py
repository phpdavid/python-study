import json

# python对象转换为json字符串
l = [1, 2, 3, 'ss', {'name': 'david', 'age': 16}]
# print(json.dumps(l, separators=[',', ':']))  # 对数据进行json编码，默认分隔符是：', ',': ',separators参数可以设置分隔符
# 对输出字典的键进行排序
d = {'a': 'a', 'c': 'c', 'b': 'b', 'd': None}
# print(json.dumps(d, sort_keys=True))  # 默认False
# json字符串转换为python对象,json.loads(): 对数据进行解码
# print(json.loads(json.dumps(d, sort_keys=True)))

# dump load和dumps loads功能是一样，但是接口不一样，前者接口是文件
# with open('test.json', 'w') as wf:  # 写入 JSON 数据
#     json.dump(json.dumps(d, sort_keys=True), wf)
with open('admin_user_20200204.json', 'r') as rf:  # 读取数据,json字符串转python字典
    admin = json.load(rf)
    print(type(admin))