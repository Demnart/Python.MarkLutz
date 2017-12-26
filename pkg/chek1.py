def minmax(test,*args):
    res = args[0]
    for arg in args[1:]:
       if test(arg,res):
           res = arg
    return res

def minim(x,y):return x < y
def max(x,y):return x > y

if __name__ == "__main__":
    print(minmax(minim,1,3,4,5,6))
    print(minmax(max,1,3,4,5,6))