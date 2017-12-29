"""Работа с методами"""

class NextClass: # Создаем класс
    # text = 'spam'
    def printer(self,text):# Каждому экземпляру класса доступен метод printer().
        self.text = text#Создаем переменную экземляра
        print(self.text)#Выводим переменную экзмпляра

if __name__ == "__main__":
    x = NextClass()
    x.printer("hello")
    print(x.text)
    y = NextClass()
    print(y.text) # Вызовет ошибку, так как в классе нет переменной text, а экзмляр класса данную переменную не создал