s = input()
ss = s.split(" ")
a = int(ss[0])
b = int(ss[1])
c = int(ss[2])

if a < b and a < c:
    if b < c:
        print(b)
    else:
        print(c)
elif b < a and b < c:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if a < b:
        print(a)
    else:
        print(b)