# Простой интерактивный цикл ввода/вывода с выходом из цикла с помощью оператора break и преобразовании полученных элементов в число
while True:
    req = input("Promt the number: ")
    if req == 'stop': break
    print(int(req) ** 3)
print('Bye')
