"""Использование лямда функций в словаре"""

key = "infor"

dictionary = {'intwo': (lambda x: x ** 2),
              'intree': (lambda x: x ** 3),
              'infor': (lambda x: x ** 4)}

print(dictionary[key](3))
