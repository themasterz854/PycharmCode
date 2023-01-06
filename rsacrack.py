import math

import sympy

n = int(input("Enter n"))
e = int(input("Enter the public key"))
p = q = 0
a = math.isqrt(n) + 1
print(a)
while True:
    b2 = a ** 2 - n
    if math.sqrt(b2) == int(math.sqrt(b2)):
        b = math.sqrt(b2)
        p = int(a + b)
        q = int(a - b)
        if sympy.isprime(p) and sympy.isprime(q) and p * q == n:
            print("p = ", p, " q = ", q)
            break
    a = a + 1

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
print("private key is ", d)

print("Enter the encrypted message")

g = input().split()

g = [int(x) for x in g]

dec = [pow(x, d, n) for x in g]

for x in dec:
    print("%c" % x, end="")
