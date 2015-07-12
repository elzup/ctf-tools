# -*- coding: utf-8 -*-

def gcd(a, b):
    if b == 0:
        u = 1
        v = 0
    else:
        q = a / b
        r = a % b
        (u0, v0) = gcd(b, r)
        u = v0
        v = u0 - q * v0
    return (u, v)

def lcm(a, b):
    return a * b / gcd(a, b)[0]

p = 171067
q = 4113
e = 65537

n = p * q

l = lcm(p - 1, q - 1)
d = gcd(e, l)[0]
if d < 0:
    d += l

# a = 20
crp = 13048
# crp = 7274
crp = 27778540
crp = 495547978
print(crp)

print(pow(crp, d, n))
