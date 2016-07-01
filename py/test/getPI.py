# get PI
from random import random
from math import sqrt
from time import clock

DARTS = 1200000000
hits = 0
clock()
for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
print('PI\'s value is %s' % pi)
print('The project runtime us %-5.5ss' % clock())