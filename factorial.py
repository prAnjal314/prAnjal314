# Create a factorial Fucnction

print("In fac(n), enter the value of n")

# Prompt user for n until he enters a positive number
while True:
	n = int(input("n: "))
	if n > 0:
		break

# Make the factorial function
def fac(k):
	j = 1
	for i in range(k):
		j = j * (i + 1)
	return j

print("Factorial", n, "equals", fac(n))
