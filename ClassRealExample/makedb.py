from ClassRealExample.person import Person,Manager

bob = Person("Bob Smith")
sue = Person("Sue Jons","developer",10000)
tom = Manager("Tom",100)

import shelve
db = shelve.open('persondb')
for object in (bob,sue,tom):
    db[object.name] = object
db.close()