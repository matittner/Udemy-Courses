"""
Mateus H. Ittner - 22/08/18
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

"""

n =  int(input("Sequence lenght: "))

a = 0
b = 1

for i in range(0,n):
	print(a)
	aux = b
	b = a
	a = a + aux
