# x = 2
# y = 52
#
# def powerOne(x,y):
#     return x ** y
#
# i = powerOne(x,y)
# print(i)
#
#  #
#  # def powOne(x, y):
#  #     return x ** y
#
#
#  # i = powOne(x, y)
"""
Функция нахождения множества
"""

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

L1 = [1,2,3,4,5,6]
L2 = [4,5,6,7,8,9]

L3 = intersect(L1,L2)
print(L3)