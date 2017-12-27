from ClassRealExample import classtools

"""Обучение работы с классами. Первый реальный приме.
Класс персона, в котором будут хранится имя фамилия, вид деятельности
и зарплата. От данного класа мы унаследуем класс Manager в котором
будем перопределять наш суперкласс"""


class Person(classtools.AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def value(self, procent):
        self.pay = int(self.pay * (1 + procent))

    def lastName(self):
        return self.name.split()[-1]




"""Мы создаем новый класс Менеджер, который
будет наследовать все методы класа Person. Так же в классе
Менеджер мы переопределим конструктор и метод value()"""


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)

    def value(self, procent, bonus=0.10):
        Person.value(self, procent + bonus)


if __name__ == "__main__":
    bob = Person("Bob Ander")
    sue = Person("Sue Armstrong", "dev", 1000)
    tom = Manager("Tom", 2000)
    bob.value(0.10)
    sue.value(0.10)
    tom.value(0.15)
    print(bob)
    print(sue)
    print(tom)
    print('#' * 300)

    class Department:
        def __init__(self, *args):
            self.members = list(args)

        def addMember(self, person):
            self.members.append(person)

        def giveRaises(self, percent):
            for person in self.members:
                person.value(percent)

        def showAll(self):
            for person in self.members:
                print(person)


    development = Department(bob, sue)  # Встраивание объектов в составной объект
    development.addMember(tom)
    development.giveRaises(.10)  # Вызов метода giveRaise вложенных объектов
    development.showAll()  # Вызов метода __str__ вложенных объектов
