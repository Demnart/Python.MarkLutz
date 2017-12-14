# Подстановка с помощью %

print("that is %d %s bird" % (1,"dead"))
print("#"*40)
eclamation = "hey!"
print("The knights say %s" % eclamation)
print("#"*40)

#Подстановка вещественных чисел разными способами
x = 1.23451
print("%e | %f | %g" % (x,x,x))
print("#"*40)
# Подстановка с отступами
x = 1234
print('...%d...%-6d...%06d' % (x,x,x))
print("#"*40)
#Подстановка вещественных чисел, с указанием знаков после запятых
print('%f | %.2f | %.*f' % (1/3.0,1 / 3.0,4,1/3.0))
print("#"*40)
#Подстановка используя списки
print("%(n)d %(x)s" % {'n':2,'x':"hello"})
print("#"*40)
#Подстановка в блоки строк
reply = """ 
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
values = {'name': 'Bob', 'age': 40} # Подготовка фактических значений
print(reply % values)


