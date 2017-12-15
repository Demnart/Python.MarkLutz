#Простой интерактивный цикл ввода/вывода с выходом из цикла с помощью оператора break и преобразовании полученных элементов в число, а так же проверку с помощью Try/Exception
while True:
    req = input("Promt the number: ")
    if  req == 'stop':
        break
    try:
        num = int(req)
    except:
        print("bad" * 8)
    else:
        print(num ** 3)
print('Bye')