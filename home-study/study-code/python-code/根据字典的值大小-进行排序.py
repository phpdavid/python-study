from random import randint

name = ['jim', 'xiao', 'zhou', 'zhao', 'lou']
data = {_: randint(80, 100) for _ in name}
# print(data)

# data = sorted(data.items(), key=lambda x: x[1], reverse=True)
# print(data)
data = sorted(zip(data.values(), data.keys()), reverse=True)
print(data)
data = {v: k for k, v in data}
print(data)
