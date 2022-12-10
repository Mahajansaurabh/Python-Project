def asum(*args):

    total=0

    for arg in args:
        if args[total]==0 and args[total+1]==0:
            return True
        else:
            total += 1
    return False

print(asum(5,6,4,0,0,10,11))