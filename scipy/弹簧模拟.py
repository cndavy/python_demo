# coding=utf-8
import numpy as np
from scipy.integrate import odeint
import pylab as pl
m=0.5
k=4
v=1
s=1
c=0.1
om = k / m
nu= c/m
def calc_deri(yvec, time, vm, om):
    return (yvec[1],- vm * yvec[1] - om * yvec[0])

#二阶方程需要被转化成一个包含向量Y =y,y'的两个一阶方程的系统。定义nu = 2 eps * wo = c / m和om = wo^2 = k/m很方便：
time_vec = np.linspace(0, 10, 100)
yarr = odeint(calc_deri, (1, 0), time_vec, args=(nu,om))

pl.plot(time_vec, yarr[:, 0], label='S')
pl.plot(time_vec, yarr[:, 1], label="V")
pl.legend()
pl.show()
