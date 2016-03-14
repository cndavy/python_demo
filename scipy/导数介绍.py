"""Solve the ODE dy/dt = -2y between t = 0..4, with the
initial condition y(t=0) = 1.
"""
from math import sin, exp, log

import numpy as np
from scipy.integrate import odeint
import pylab as pl
from sympy.mpmath import ln


def calc_derivative(ypos, time):
    return  -2*ypos

#y=x^2
time_vec = np.linspace(-4, 4 , 400 )
yvec = odeint(calc_derivative, exp(8), time_vec)
yy=   np.exp(-2*(time_vec))
pl.plot(time_vec,yvec)
pl.plot(time_vec, yy )
pl.xlabel('Time [s]')
pl.ylabel('y position [m]')
pl.show()

