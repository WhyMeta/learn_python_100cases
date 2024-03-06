import math


# print("圆面积", math.pi)

def get_area(r):
    # math.pi 是圆周率 3.141592653589793，r 是半径，使用 round 保留小数后4四位四舍五入输出
    return round(math.pi * r * r, 4)


print("半径为2，圆面积", get_area(2))
print("半径为3.14，圆面积", get_area(3.14))
print("半径为8.1786，圆面积", get_area(8.1786))
