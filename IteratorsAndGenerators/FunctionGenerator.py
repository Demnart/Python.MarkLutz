"""Пример первой функции генератора"""

def senq(N):
    for x in range(N):
        yield x ** 2


for i in senq(5):
    print(i, end=':')