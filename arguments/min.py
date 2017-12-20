"""Функции определяющие минимум"""
""" Функция min1() принимает в себя кортеж значений и определяет минимальный элемент"""
def min1(*args):
    res = args[0]
    for i in args[1:]:
        if i < res:
            res = i
    return res

def min2(params,*args):
    for i in args:
        if i < params:
            params = i
    return params

def min3(*args):
    L = list(args)
    L.sort()
    return L[0]

print(min1(1,4,56,8,-19))
print(min2(10,123,54,5,1))
print(min3([1,1],[1,2],[1,0]))