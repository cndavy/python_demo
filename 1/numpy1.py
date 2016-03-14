from numpy.testing import assert_

__author__ = 'han'

import numpy as np
print (type(np.array([1.,2,3,4])))
print (np.zeros((3,4)))
print (np.ones((3,4)))
print (np.eye(3))
for x in np.linspace(1,3,3):
    print (x)

a = np.ones((2,2))
b = np.eye(2)
print (a)
print (b)
print (a+b)
import scipy
scipy.test("fast")

