'''
差分&均差
（暂时无法绘制表格）

dif()
    计算1阶差分
    输入:
        序列Y
    输出:
        1阶差分序列dif_Y

div_dif()
    计算1阶均差
    输入:
        序列Y
    输出:
        1阶均差序列dif_Y

hdif()
    计算n阶差分
    输入:
        序列Y, 阶n
    输出:
        n阶差分序列hdif_Y

hdiv_dif()
    计算n阶均差
    输入:
        序列Y, 序列X, 阶n
    输出:
        n阶差分序列hdiv_Y

2022/1/25
'''

# caculate the differences of Y
def dif (Y):
    dif_Y = []
    for i in range(len(Y) - 1):
        dif_Y.append(Y[i+1] - Y[i])

    return dif_Y

# caculate the divided differences of Y
def div_dif (Y, X = None):
    if X == None:
        X = list(range(len(Y)))

    div_Y = []
    for i in range(len(Y) - 1):
        div_Y.append((Y[i+1] - Y[i]) / (X[i+1] - X[i]))

    return div_Y

# caculate the high order differences of Y
def hdif (Y, n = None):
    if n == None:
        n = 1

    # iterate dif() for n times
    hdif_Y = Y
    for i in range(n):
        hdif_Y = dif(hdif_Y)

    return hdif_Y

def hdiv_dif (Y, X = None, n = None):
    if n == None:
        n = 1
    
    # iterate div_dif() for n times
    hdiv_Y = Y
    for i in range(n):
        hdiv_Y = div_dif(hdiv_Y, X)

    return hdiv_Y


if __name__ == '__main__':
    X = eval(input('X: '))
    Y = eval(input('Y: ')) 
    n = eval(input('n: '))

    for i in range(n):
        print(str(i) + ': ' + str(hdiv_dif(Y, X, i+1)))
