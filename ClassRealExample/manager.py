import person

class Manager(person.Person):

    def percent(self,percent,bonus = .10):
        Person.percent(self,percent + bonus)

