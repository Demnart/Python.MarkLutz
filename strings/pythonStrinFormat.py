#Форматирование строк в питоне используя метод format
#Форматирование подстановкой где цифра обозначает позицию элемента в методе format
template = '{0},{1} and {2}'
print(template.format("spam","ham","eggs"))
print("#"*40)

#Форматирование по именованным переменным
template = '{motto},{pork} and {food}'
print(template.format(motto="spam", pork="ham", food="eggs"))
print("#"*40)

#Фороматирование по 1 и 2 варианту
template = '{motto},{0} and {food}'
print(template.format("spam", motto = "ham", food = "eggs"))
print("#"*40)

x = "{motto},{0} and {food}"
x.split('and')
print(x.format("spam", motto = "eats",food = "eggs"))

x = 's,pa,m'
y = x.split(',')
print(y)
x = "/".join(y)
print(x)
z = x[ : 1] + x[2 : 4] +x[5:]
print(z)