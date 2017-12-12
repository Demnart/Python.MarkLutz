string = "Spam"
# Базовые операции со строками и последовательностями
print(len(string))
print(string[0],end="")
print(string[1])
# В последовательностях мы можем производить индексацию справа на лево, первый индекс же будет равен -1
print(string[-1],end="")
print(string[-2])

#Срезы
print(string[:])
print(string[1:2])
print(string[0:-1])
print(string[1:2])

#Конкатенация

print(string + "Hello")

#Множественное повторение

print(string * 8)
