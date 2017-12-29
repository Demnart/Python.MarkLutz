"""Пример наследования, перопределения и организации класов"""


class Super:

    def method(self):
        print("In Super class")

    def delegate(self):
        self.action()


class Inherrit(Super):
    pass


class Replacer(Super):
    def method(self):
        print("In Replacer class")


class Extender(Super):
    def method(self):
        print("Start Extender class")
        Super.method(self)
        print("End Extender class")


class Provider(Super):
    def action(self):
        print("In Provider class")


if  __name__ == "__main__":

    for klass in (Inherrit,Replacer,Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()


