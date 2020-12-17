import math as mt

dcml = int(input("decimal: "))
n = dcml
m = ""
l = mt.log(n, 2)
o = int(l)

for i in range(o):
    if n / 2 == 0:
        m = m + "0"
    elif n / 2 == 1:
        m = m + "1"
    n = int(n/2)
    print(n)
    m = m[::-i-1]
    print(m)
