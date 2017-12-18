"""Функция регкурсия"""

def recursion(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + recursion(L[1:])

l=recursion([1,2,3,4,5])
print(l)