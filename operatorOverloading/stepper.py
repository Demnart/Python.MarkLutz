"""Перегрузка оператора getiter как итератора
по индексам"""

class Stepper:
    def __getitem__(self, item):
        return self.data[item]

if __name__ == "__main__":
    x = Stepper() # Создаем экземпляр класса
    x.data = "spam"# Устанавливаем значение переменной для экземпляра класса
    print(x[1])

    for c in x:         # При работе цикла for вызывается __getitem__()
        print(c,end="")
    print('p' in x)
    L = [c for c in x]
    print(L)
    print(list(x),tuple(x), ','.join(x))
