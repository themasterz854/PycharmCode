"""mod 37
x = input()
x = x.split(" ")
for y in x:
    y = int(y)
    r = y % 37
    if r in range(0, 26):
        ans = chr(ord('A') + r)
    elif r in range(26,35):
        ans = r-26
    else:
        ans = '_'
    print(ans,end="")"""

# mod 41
x = input()
x = x.split(" ")
for y in x:
    y = int(y)
    r = y % 41
    i = pow(r, -1, 41)
    if i in range(1, 27):
        ans = chr(ord('A') + i)
    elif i in range(27, 37):
        ans = i - 27
    else:
        ans = '_'
    print(ans, end="")
