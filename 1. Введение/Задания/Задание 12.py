import math

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

AB = (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
BC = (math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2))
AC = (math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2))

Pabc = AB + BC + AC
p = Pabc / 2
print(Pabc, math.sqrt(p * (p - AB) * (p - BC) * (p - AC)))
