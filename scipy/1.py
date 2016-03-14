
from numpy.ma import zeros
from scipy.fftpack import fft
from pylab import *

import numpy as np

a = zeros(1000)
a[:100]=1
c=sin(a)
b = fft(a)
show()

f=arange(-500,500,1)
grid(True)
plot(f,abs(concatenate((b[500:],b[:500]))))
show()
