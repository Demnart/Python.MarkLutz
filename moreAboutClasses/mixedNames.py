"""Пример использования переменной класса и переменной которая инициализируется в конструкторе класса."""


class ClassName:
    data = 'spam' # Создаем класс и определяем переменную класса

    def __init__(self, value): #Создаем конструктор класса с обязательным указанием переменной экземляра data
        self.data = value # Переменная data будет отличаться для каждого экземпляра класа

    def changeData(self): # Создаем метод changeData(self) не принимающий аргументов. Его главная задача изменить переменную data экземляра класса
        self.data = "hello"


if __name__ == "__main__":

    x = ClassName('Artiom')
    y = ClassName('Alina')
    print("Now x is {}".format(x.data))
    print("Now y is {}".format(y.data))
    print("Variable data of ClassName.data is {}".format(ClassName.data))

    x.changeData()
    y.changeData()
    print("After using method ClassName.changeData()")
    print("Now x is {}".format(x.data))
    print("Now y is {}".format(y.data))
    print("Variable data of ClassName.data is {}".format(ClassName.data))
