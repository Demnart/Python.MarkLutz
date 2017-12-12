dictionary = {'food': 'spam','quantity':3,'color':'blue'}

print(dictionary)

#Вывод значения словаря по ключу
print(dictionary['food'])
print("##################################")
#Создание словаря и присвоенеие ему ключей и значений
d ={}
d['name'] = "Artiom"
d['surname'] = "Rogov"
d["age"] = 24

print(d)

print("###nesting###")
#Вложенность в словарях и использование списка
v = {"name" : {"first": "artiom","last":"rogov"},
     "job":["dev","mngr"],
     "age":"24.7"}

print(v["name"])
print(v["name"]["first"])
v["job"].append("janitor")
print(v)