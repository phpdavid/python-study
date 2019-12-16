# 字典代替switch语句
# day = 6
# switcher = {
#     0:'sun',
#     1:'mon',
#     2:'tues'
# }
#
# switch = switcher.get(day,'unknow')
#
# print(switch)
day = 1


def get_sun():
    return "sun"


def get_mon():
    return "mon"


def get_tues():
    return "tues"


def get_default():
    return "unknow"


switcher = {
    0: get_sun,
    1: get_mon,
    2: get_tues,
}
switch = switcher.get(day, get_default)

print(switch())
