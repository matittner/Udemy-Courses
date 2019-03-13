"""
Mateus H. Ittner - 22/08/18

Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

"""

def findPrime(n):
	"""
	Searches for the first prime after a number N
	"""
	while True:
		for i in range(2,n): # checks if prime
			if n % i == 0 and i != n:
				break
		else:
			return n # if yes, returns the number
		n += 1  #else, tries the next number

prime = 1

while input("Next? (n to quit) ").lower() != 'n':
	print(prime)
	prime = findPrime(prime + 1) # pass next number
	


