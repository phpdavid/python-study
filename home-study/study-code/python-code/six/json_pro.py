import json

# 反序列操作
# # json中不止一种数据格式，还有object对象，array数组，str字符串
# json_str = '{"name":"david"}'  # json字符串在js中是一个对象，在pythonh中是一个字典
# json_array = [{"name": "david"}, {"name": "david"}]  # 有两个对象的json数组，组数就是一个集合
# # 文件命名不能使用json
# student = json.loads(json_array)  # 转换为有两个字典的列表
# # student = json.loads(json_str) #转换为字典
# print(type(student))
# 序列化操作（mangodb比较适合存储序列化后的对象，强烈反对将数据序列化后存入数据库）
py_list = [{'name': 'david', 'age': 15, 'flag': False},
           {'name': 'Lili', 'age': 16, 'flag': True}]

r = json.dumps(py_list)  # python list转换为json字符串
print(r)
