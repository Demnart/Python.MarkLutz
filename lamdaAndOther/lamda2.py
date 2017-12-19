"""Вложеные лямда функции"""

f = (lambda x: lambda y,z: x+y+z)

fun = f(1)
zipp =fun(5,3)

print(zipp)