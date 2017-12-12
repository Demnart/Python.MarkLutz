list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(list)
#С помощью генератора получаем 2 столбец вложенного списка под индексом 1
col2 = [row[1] for row in list]
print(col2)
#С помощью генератора получаем 2 столбец вложенного списка и прибавляем к его значениям единицу
col2a = [row[1] + 1 for row in list]
print(col2a)
#С помощью генератора получаем 2 столбец и отображаем только четные числа
col2b = [row[1] for row in list if row[1] % 2 == 0]
print(col2b)
#с помощью генератора получаем диагональ списка
diag = [list[i][i] for i in [0,1,2]]
print(diag)