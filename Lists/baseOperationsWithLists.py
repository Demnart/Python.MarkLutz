#Создание списка из непрерывной последовательности целых чисел
l = list(range(-4,4))

# Итерация по списку
print('# Итерация по списку')
for i in l:
    print(i)
print("#"*40)

#Генератор списков
print('#Генератор списков')
s = "spam"
rec = [c * 4 for c in s]
print(rec)
print("#"*40)

#Эквивалент генератора списка
print("#Эквивалент генератора списка")
rec=[]
s = "spam"
for i in s:
    rec.append(i*4)
print(rec,end="")
print()
print("#"*40)

#Встроенная функция map
print("Встроенная функция map")
l = list(map(abs,[-1,0,1,2,3]))
print(l)

print("#"*80)
print("СРЕЗЫ/ИНДЕКСЫ/МАТРИЦЫ")

l = ['spam','Spam','SPAM']
#Получение обьекта с индексом 1
print("#Получение обьекта с индексом 1")
print(l[0])
#Получение обьекта с индексом -2
print("#Получение обьекта с индексом -2")
print(l[-2])
#Получения среза с 1 элемента и до конца списка
print("#Получения среза с 1 элемента и до конца списка")
print(l[1:])
print("#"*40)

print("Матрицы или вложеные списки")
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#Получения 1 вложенного списка, целиком
print("#Получения 1 вложенного списка, целиком")

print(matrix[0])
#Получение 2 элемента во втором вложенном списке
print("#Получение 2 элемента во втором вложенном списке")
print(matrix[1][1])


