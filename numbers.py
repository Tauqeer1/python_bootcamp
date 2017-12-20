# allow you to import capabilities from python3 to python 2
from __future__ import division

a = 2 + 2 - 2
print(a)
b = 2 * 3
print b
# In python 2 the number after decimal has truncated, but in python 3 it is not true anymore
c = 3 / 2
print c  # result in integer c = 1
d = 3.0 / 2
print d  # result in float d = 1.5
e = 3 / 2.0
print e  # result in float e = 1.5
f = float(3) / 2
print f
g = 3 / float(2)
print g
h = 1 / 2
print h

# Taking power
print 2**3
