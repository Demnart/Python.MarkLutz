# string = "AAA"
#
# for s in string:
#     print(ord(s))

# string = "AAA"
# L = []
# for s in string:
#     L.append(ord(s))
# print(L)

# for i in range(50):
#     print("hello %d\n\a" % i )

# D = {'a' : '1', 'b' : 2 , 'c' : 3,7:"a",2:'32',1:'adab'}
#
# for i in sorted(D.keys()):
#     print(i , '=>' , D[i])


L = []
for i in range(6):
    L.append(2**i)
print(L)

D = [2 ** x for x in range(10)]
print(D)

print(list(map(lambda x:2**x,range(7))))