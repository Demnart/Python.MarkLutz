"""Переменная класса, доступна всем экземплярам класса если она не будет переопределена экземпляром"""


class Shared:
    data = "spam"

    """Данный метод изменяет область видимости переменной data и изменяет ее значение, причем значение индивидуально для каждого экземпляра
        self.data = value"""

    def changeData(self,value):
        self.data = value

if __name__ == "__main__":
    x = Shared()
    y = Shared()

    Shared.data = 'Minimum' #Изменение переменной класса, через обращение имени класса.

    print('x = {}'.format(x.data))  # Экземпляры класса
    print('y = {}'.format(y.data))  # Экземпляры класса
    print('Class.data = {}'.format(Shared.data))  # Обращение напрямую через вызов имени класса

    x.changeData("hello")
    y.changeData("Mideo")

    print("After using class method Shared.changeData(...)")
    print('x = {}'.format(x.data))  # Экземпляры класса
    print('y = {}'.format(y.data))  # Экземпляры класса
    print('Class.data = {}'.format(Shared.data))  # Обращение напрямую через вызов имени класса


