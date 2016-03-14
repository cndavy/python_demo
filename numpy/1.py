import time
import math

__author__ = 'han'
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print  a[1]
print  a[3:6]
print a.ndim
print a.shape
print a.dtype
print len(a)
print a[::-1]
print "-------"
b = np.array([[0, 1, 2], [3, 4, 5]])
print b
print b.ndim
print b.shape

print len(b)

print "-------"
c = np.array([[[1], [2]], [[3], [4]]])
print( c)

print c.shape

d = np.linspace(0, 1, 5)
print d

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
# plt.plot(x, y)  # line plot
#
# plt.plot(x, y, 'o')  # dot plot
# plt.show()
#
# image = np.random.rand(30, 30)
# plt.imshow(image, cmap=plt.cm.hot)
# plt.colorbar()
# plt.show()

persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']})
a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)],
             dtype=persontype)

print a

print a.dtype

x = [i * np.pi*0.1 for i in xrange(100)]
x = np.array(x)
start = time.clock()
y=np.sin(x)
print "numpy.sin:", time.clock() - start

plt.plot(x, y)  # dot plot
plt.show()