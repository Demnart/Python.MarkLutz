x = 11  # Глобальная переменная модуля


def f():
    print(x)  # Глобальная переменная модуля


def g():
    x = 22  # Локальная переменная функции
    print(x)  # Вывод локальной переменной


class Names:
    x = 44  # Пеменная класса

    def func(self):
        x = 23  # Локальная переменная метода
        self.x = 15  # Установка дефолтного значения для переменной x экземляра класса


if __name__ == "__main__":
    print(x)
    f()
    g()
    print(Names.x)
    var = Names()
    print(var.x)
    var.func()  # При вызове данного метода экземпляру класса var будет присвоено значение переменной х по умолчанию равной 15 и это значение перезатрет значение переменной классасдф
    print(var.x)