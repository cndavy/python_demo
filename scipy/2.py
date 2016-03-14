# coding=utf-8
import numpy as np
from scipy.integrate import odeint
import pylab as pl

mass = 0.5
kspring = 4
cviscous = 0.4

nu_coef = cviscous / mass
om_coef = kspring / mass
eps = cviscous / (2 * mass * np.sqrt(kspring / mass))
print ( "eps=" , eps)


def calc_deri(yvec, time, nuc, omc):
    return (yvec[1], -nuc * yvec[1] - omc * yvec[0])

#二阶方程需要被转化成一个包含向量Y =y,y'的两个一阶方程的系统。定义nu = 2 eps * wo = c / m和om = wo^2 = k/m很方便：
time_vec = np.linspace(0, 10, 100)
yarr = odeint(calc_deri, (1, 0), time_vec, args=(nu_coef, om_coef))

pl.plot(time_vec, yarr[:, 0], label='y')
pl.plot(time_vec, yarr[:, 1], label="y'")
pl.legend()
pl.show()
