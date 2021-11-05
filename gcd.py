

a = int(input())
b = int(input())

if(a == b):
        print(a)
        exit(0)
else:
    if (a < b):
        a, b = b, a
    while( b != 0):
        m = a % b
        if m == 0:
            print(b)
            break
        a = b
        b = m




