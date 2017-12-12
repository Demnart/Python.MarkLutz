#Оригинальный список
list = [1,'spam',2,3]
print(list)
#В список был добавлен 1 элемент в конец списка
list.append('Ni')
print(list)
# Из списка удален элемент, позиция которого равна индексу 2
list.pop(2)
print(list)
#Вставить элемент в список по указанному индексу
list.insert(2,"hello")
print(list)
#Удалить элемент списка по значению
list.remove("spam")
print(list)

print()
print("#############################################")
print()
#Сортировка списка
list1 = ["aa","cc","bb"]
list1.sort()
print(list1)
#Реверс списка
list1.reverse()
print(list1)