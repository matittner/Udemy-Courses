"""
Mateus H. Ittner - 22/08/18
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

"Prime Factorization" is finding which prime numbers multiply together to make the original number.

"""

def findFirstDivisiblePrime(n):
	"""
	Searches for the first divisible prime of a number N
	"""
	for i in range(2,n + 1): # from 2 to itself (inclusive)
		for j in range(2,i): 
			if i%j == 0 and j != i: # tests if prime, if any number is divisible, it's not a prime and the loop ends
				break	            # if j == i, it means the number is prime
		else:
			if n%i == 0:  # if it's a prime number and divisible by N, returns the number
				return i 

n =  int(input("Input number: "))

while n != 1:
	prime = findFirstDivisiblePrime(n)
	print(prime)
	n = int(n / prime)


