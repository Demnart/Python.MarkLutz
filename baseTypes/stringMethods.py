s = "Spam"
#Писк по строке и указание на индекс 1-го попавшегося элемента соответствующего заданным условиям
print(s.find("pa"))
#Изменение строки
print(s.replace('pa','XYZ'))
#Разделение строки на список,
line = "aaa,bbb,ccccc,eeee"
splitLine = line.split(',')
print(splitLine)
#Перевод в верхний регистр
string = s.upper()
print(string)
#Проверка на то нет ли в строке символов алфавита, если есть другие символы возвращает False
alpha = s.isalpha()
print(alpha)






