"""Пример выражения генераторов"""

G = (x **2 for x in range(4))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))