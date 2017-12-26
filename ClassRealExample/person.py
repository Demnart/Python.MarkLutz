"""Создаем наш класс Person для учебных целей и для получения практики раб
оты с классами и ООП вцелом"""

class Person:
    """ """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]

    def percent(self,percent):
        self.pay = int(self.pay * (1 + percent))


    def __str__(self):
        return '[Person : {},{},{}]'.format(self.name,self.job,self.pay)
if __name__ == "__main__" :

    bob = Person("Bob Smith")
    sue = Person("Sue","Manager",1500)
    elise = Person("Elise","Developer")
    print(bob.name,bob.job,bob.pay)
    print(sue.name,sue.job,sue.pay)
    print(sue.lastName(),bob.lastName())
    print(bob)
    print(sue)
