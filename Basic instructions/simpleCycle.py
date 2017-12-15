#Простой интерактивный цикл ввода/вывода с выходом из цикла с помощью оператора break
while True:
    request = input("Enter text: ")
    if request == 'stop': break
    print(request.upper())
