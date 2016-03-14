#coding: utf-8
__author__ = 'han'
import numpy as np
from scipy import integrate

def half_circle(x):
    return (1-x**2)**0.5
#积分半圆球


def half_sphere(x, y):
    return (1-x**2-y**2)**0.5
pi_half, err = integrate.quad(half_circle, -1, 1)
print pi_half*2
#二重积分 x= -1 1 y =
v,err1=integrate.dblquad(half_sphere, -1, 1,
    lambda x:-half_circle(x),
    lambda x:half_circle(x))

print  u"积分结果=",  v
print  u"公式计算=" ,(np.pi*4/3)/2
# 通过球体体积公式计算的半球体积
#2.0943951023931953

