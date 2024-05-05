def add (*args):
    total = 0
    for n in args:
        total = total+n
    return total

print(add(1,2,3,4,5))