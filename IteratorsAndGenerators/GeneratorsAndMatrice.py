"""Генераторы списка и матрицы"""

M = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

N = [
    [2,2,2],
    [3,3,3],
    [4,4,4]
]

print([M[row][1] for row in (0,1,2)])

"""Использование функции range() для прохода матрицы по диогонали"""

print([M[i][i] for i in range(len(M))])
print(len(M))