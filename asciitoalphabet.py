i = 1
x = input().split(", ")
print(x)
n = len(x)
j = 0
ans = ""
while (j < n):
    i = int(x[j])
    if (i == 28):
        ans = ans + "_"
        j += 1
        continue
    if (i == 27):
        ans = ans + " "
        j += 1
        continue

    ans = ans + chr(i - 1 + ord('a'))
    j += 1

print(ans)
