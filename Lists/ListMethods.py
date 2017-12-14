l = ['spam','Spam','SPAM']
#Добавление в список с помощью метода .append()
print("Добавление в список с помощью метода .append()")
l.append('spaM')
print(l)
print("#"*40)
#Сортировка методом .sort(). Следует помнить, что сортировка производится по таблице ASCII
print("Сортировка методом .sort(). Следует помнить, что сортировка производится по таблице ASCII")
l.sort()
print(l)
print("#"*40)
#Сортировка методом .sort() используя ключ, по которому будет определяться как будет происходить сортировка. Следует помнить, что сортировка производится по таблице ASCII
print("#Сортировка методом .sort() используя ключ, по которому будет определяться как будет происходить сортировка. Следует помнить, что сортировка производится по таблице ASCII")

l = ['abc','aBe','ABD']
l.sort()
print("Обычная сортировка")
print(l)
print("Сортировка с ключом")
l.sort(key=str.lower)
print(l)
print("#"*40)
#Добавление нескольких элементов в конец списка .extend()
print("метод добавление нескольких элементов в конец списка .extend()")
l = [1,2]
l.extend([3,4,5])
print(l)
#Метод удаления последнего элемента в списке pop()
print("Метод удаления последнего элемента в списке pop()")
l.pop()
print(l)
print("#"*40)
# Метод смены следования доменов .reverse()
print("Метод смены следования доменов .reverse()")
l.reverse()
print(l)
print("#"*40)
# Встроення функция в list, функция сортировки в обратном порядке l = list(reversed())
print("# Встроення функция в list, функция сортировки в обратном порядке")
L=[4,3,2,1]
l = list(reversed(L))
print(l)
print("#"*40)
#Метод для поиска индекс нашего обьекта в списке
print("Метод для поиска индекс нашего обьекта в списке")
L = ["spam","eats","eggs"]
print(L.index("spam"))
print("#"*40)
#Метод для вставки значений в определенный индекс .insert()
print("Метод для вставки значений в определенный индекс .insert()")
L.insert(2,"toasts and")
print(L)
print(" ".join(L))
print("#"*40)
#Удаление обьекта с определенным значением с помощью метода .remove()
print("#Удаление обьекта с определенным значением с помощью метода .remove()")
L.remove("eggs")
print(L)
print("#"*40)

















