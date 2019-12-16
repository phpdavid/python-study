"""
一段小程序
"""
user = 'abc'
pwd = 'abc123'
print('please input your username')
user_input = input()
print('please input your password')
pass_input = input()

if user_input == user and pass_input == pwd:
    print('welcome')
elif user_input != user and pass_input == pwd:
    if not(1+1 < 2):
        print('1+1 ==2')
    else:
        print('great')
    print('username is wrong')
elif user_input == user and pass_input != pwd:
    print("password is wrong")
elif user_input != user and pass_input != pwd:
    print("username and password are wrong")
else:
    print('username or password is wrong')


