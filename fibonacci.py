a = 1
b = 0
n = int(input("n: "))
fibo = []

for i in range(n):
	a = a + b
	b = b + a
	fibo.append(a)
	fibo.append(b)
print(fibo[0:n-1])