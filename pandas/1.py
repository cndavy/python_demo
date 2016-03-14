import pandas as pd
import numpy as np
import matplotlib as pl
import scipy as sp

s = pd.Series([1, 3, 5, 6, np.nan, 7, 8])

print s

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print s

d = {'a': 0., 'b': 1., 'c': 2.}
print pd.Series(d)
print pd.Series(d, index=['b', 'c', 'd', 'a'])

multIndex = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                          ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                          ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                          ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                          ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})

# print multIndex
multIndex = pd.DataFrame({('a'): {('A'): 1} })
print multIndex