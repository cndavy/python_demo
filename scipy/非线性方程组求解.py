# coding: utf-8
__author__ = 'han'
from scipy.optimize import fsolve
from math import sin, cos


def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
        5 * x1 + 3,
        4 * x0 * x0 - 2 * sin(x1 * x2),
        x1 * x2 - 1.5
    ]


result = fsolve(f, [1, 1, 1])

print result
print f(result)

"""

雅可比矩阵

雅可比矩阵是一阶偏导数以一定方式排列的矩阵，它给出了可微分方程与给定点的最优线性逼近，
因此类似于多元函数的导数。例如前面的函数f1,f2,f3和未知数u1,u2,u3的雅可比矩阵如下

"""


def j(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    # f 的导数偏导
    return [
        [0, 5, 0],
        [8 * x0, -2 * x2 * cos(x1 * x2), -2 * x1 * cos(x1 * x2)],
        [0, x2, x1]
    ]


result = fsolve(f, [1, 1, 1], fprime=j)
print result
print f(result)
