origin = 0


# 闭包实例

def curve_pro(pos):
    def curve(x):
        nonlocal pos  # 声明不是局部变量
        new_pos = pos + x
        pos = new_pos
        return new_pos
        # return pos * x

    return curve


f = curve_pro(origin)
print(f(2))
print(f(5))
print(f(8))
print(f.__closure__)
