D = {'a' : 'hello' , 'b' : ',' , 'c' : ' world!'}

ks = list(D.keys())

print(ks)

ks.sort()

for key in ks:
    print(key, "=>",D[key])

print(D)