from math import log2
res = int(log2(64)) + 2 ** abs(1+1j)
print("(a) res = ", res )
from math import sqrt, floor, ceil
res = floor(2.3 * 7) * ceil(2 ** 3 + 7.1)
print("(b) res = ",res )
from math import pi, sin, cos, radians
res = cos(pi/4)**2 + sin(radians(45))**2j
print("(c) res = ",res )
res = 6 * round(2.1, 1) // 1
print("(d) res = ",res )
