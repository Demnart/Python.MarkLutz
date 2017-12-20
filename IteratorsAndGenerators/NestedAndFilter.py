"""Получение четных чисел с помощью: 1. Генератора списков, 2. Функции filter(), 3 Цикла for"""

x = [x for  x in range(10) if x % 2 == 0 ]
print(x)

print('#'*100)

x = list(filter((lambda x : x % 2 == 0), range(10)))
print(x)
print('#'*100)


res = []

for x in range(10):
    if x % 2 == 0:
        res.append(x)

print(res)
