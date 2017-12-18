"""Использовании лямда функции в словаре"""

L = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

for i in L:
    print(i(2))

print(L[2](14))