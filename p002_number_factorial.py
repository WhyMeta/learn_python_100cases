# 1. 数字的阶乘（factorial）是指从1到该数字所有整数的乘积。例如，数字5的阶乘表示为5!，其计算如下：
# 例子：5! = 5 × 4 × 3 × 2 × 1 = 120
# 2. 通常，阶乘可以用递归或迭代的方式进行计算。
# 3. 求：5的阶乘，10的阶乘

def get_factorial_for(n):
    result = 1  # 定义一个变量，用于存储阶乘的结果，初始值为1，因为任何数字的阶乘都至少是 1
    equation = ""  # 初始化阶乘算式为空字符串
    # 使用 for 循环迭代从 1 到 n 的所有整数，包括 n，循环体内用于计算数字 n 的阶乘
    for i in range(1, n + 1):
        # 在循环体内，每次迭代将 i 乘以 result，然后将结果赋值给 result
        # 这样就实现了从 1 到 n 所有数字的连乘，最终得到 n 的阶乘
        result *= i
        if i == 1:
            # 如果 i 是第一个数，直接添加到算式中
            equation += str(i)
        else:
            # 如果 i 不是第一个数，将 i 与 " × " 连接
            equation += " × " + str(i)
    return result, equation  # 返回最终的结果


def get_factorial_while(n):
    result = 1  # 定义一个变量，用于存储阶乘的结果，初始值为1，因为任何数字的阶乘都至少是 1
    equation = str(n)  # 用于保存阶乘的计算式，转换为字符串，方便后续打印
    while n > 1:
        # 在循环体内，每次迭代将 n 乘以 result，然后将结果赋值给 result
        # 这样就实现了从 n 到 1 所有数字的连乘，最终得到 n 的阶乘，
        result *= n
        # 如果 n > 1，将 n 与 " × " 连接，否则将 n 与 "x" 连接
        equation += " × " + str(n - 1) if n > 1 else " x 1"
        # 在循环体内，将 n 的值减1，这是为了在每次迭代中计算下一个数字的乘积，直到 n 减少到1为止。
        n -= 1

    return result, equation  # 返回最终的结果


# for 循环方法
print("for 循环方法：")
# print("阶乘 5 的结果 = ", get_factorial_for(3))  # 5的阶乘
# print("阶乘 10 的结果 = ", get_factorial_for(6))  # 10的阶乘
result, equation = get_factorial_for(5)
print("阶乘 5 的结果 = ", result)  # 5的阶乘
print("阶乘 5 的计算式 = ", equation)  # 5的阶乘算式

result, equation = get_factorial_for(10)
print("阶乘 10 的结果 = ", result)  # 10的阶乘
print("阶乘 10 的计算式 = ", equation)  # 10的阶乘算式

# while 循环方法
print("=" * 50)
print("while 循环方法：")
# print("阶乘 5 的结果 = ", get_factorial_while(5))  # 5的阶乘
# print("阶乘 10 的结果 = ", get_factorial_while(10))  # 10的阶乘

result, equation = get_factorial_while(5)
print("阶乘 5 的结果 = ", result)  # 5的阶乘
print("阶乘 5 的计算式 = ", equation)  # 5的阶乘算式

result, equation = get_factorial_while(10)
print("阶乘 10 的结果 = ", result)  # 10的阶乘
print("阶乘 10 的计算式 = ", equation)  # 10的阶乘算式