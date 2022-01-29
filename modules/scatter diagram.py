'''
绘制散点图（含X轴变换）

transform(Y, X = None)
    对X进行变换（注意Y, X 的顺序）
    目前仅支持math模块内的函数
    输入:
        列表Y
        列表X = None
    键入: 
        变换函数，如 "math.sqrt"
        x轴的基  = None
draw_plot(Y, X = None)
    绘制散点图（注意Y, X 的顺序）
    输入:
        列表Y
        列表X

2022/1/24
'''

import matplotlib.pyplot as plt
import math

# Draw the scatter diagram
def draw_plot(Y, X = None):
    plt.plot(X, Y, 'o')
    plt.show()

# 对 X 进行变换
def transform(Y, X = None):
    # X 默认为 range
    if X == None:
        X = list(range(len(Y)))

    # 键入变换函数
    function = input('trans_function: ')

    for i in range(len(X)):
        # 分别对 X 的每一项进行变换
        X[i] = eval(function + '(X[{}])'.format(str(i)))

    # 显示 X 轴变换后的基
    base = input('Base of X: ')
    plt.xlabel(base)

    return X

if __name__ == '__main__':
    X0 = eval(input("The data of X(None): "))
    Y = eval(input("The data of Y: "))

    # try, try and try again
    while True:

        X = transform(Y, X0)
        draw_plot(Y, X)

        flag = input('Quit? (N/Y)')
        if flag == 'Y':
            break