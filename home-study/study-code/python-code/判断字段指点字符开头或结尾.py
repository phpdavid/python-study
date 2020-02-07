import os, stat

# 读取py格式和txt格式，修改权限
res = [name for name in os.listdir('.') if name.endswith(('.py', '.txt'))]  # endwith 可以传入一个元祖
# oct(os.stat('__init__.py').st_mode)#查看文件的权限

os.chmod('__init__.py', os.stat('__init__.py').st_mode | stat.S_IXUSR)  # 加上用户可执行权限
print(oct(os.stat('__init__.py').st_mode))
