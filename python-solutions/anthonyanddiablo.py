"""
pi * r^2 = area
2 * pi * r = cir

r = cir/(2*pi)

area = r**2 * pi
"""

from math import pi

a, n = map(float, input().split())
r = n/(2*pi)
max_area = (r**2) * pi
if max_area >= a:
    print("Diablo is happy!")
else:
    print("Need more materials!")