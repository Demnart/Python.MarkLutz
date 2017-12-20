

def adder(**a):
    args = list(a.values())
    tot = args[0]
    for i in args[1:]:
        tot += i
    return tot

def adder1(**args):
    arg = list(args.keys())
    tot = args[arg[0]]
    for i in arg[1:]:
        tot += args[i]
    return tot