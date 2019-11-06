def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 4
    return damage1, damage2  # 直接return多个结果


# damages = damage(6, 9)
# print(damages, type(damages))  # 返回的结果是tuple

damages_result1, damages_result2 = damage(99, 66)  # 赋值给两个变量，有助于代码更加的清晰
print(damages_result1, damages_result2)
