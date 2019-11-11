import json

# json中不止一种数据格式，还有object对象，array数组，str字符串
json_str = '{"name":"david"}'  # json字符串在js中是一个对象，在pythonh中是一个字典
json_array = [{"name": "david"}, {"name": "david"}]  # 有两个对象的json数组，组数就是一个集合
# 文件命名不能使用json
student = json.loads(json_array)  # 转换为有两个字典的列表
# student = json.loads(json_str) #转换为字典
print(type(student))
