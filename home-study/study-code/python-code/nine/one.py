#字典代替switch语句
day = 6
switcher = {
    0:'sun',
    1:'mon',
    2:'tues'
}

switch = switcher.get(day,'unknow')

print(switch)
