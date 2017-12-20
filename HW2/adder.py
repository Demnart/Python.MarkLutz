"""1 ВАРИАНТ"""

def adder1(*args):
    print('adder1',end="")
    if type(args[0]) == type(0):
        sum = 0
    else:
        sum = args[0][:0]
    for arg in args:
        sum += arg
    return sum

def adder(*arg):
    sum = arg[0]
    for i in arg:
        sum += i
    return sum

