"""
Mateus H. Ittner - 22/08/18

Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.


How to convert decimal to binary
Conversion steps:
Divide the number by 2.
Get the integer quotient for the next iteration.
Get the remainder for the binary digit.
Repeat the steps until the quotient is equal to 0.

bin to dec
The decimal number is equal to the sum of binary digits (dn) times their power of 2 (2n):

"""

op = input("1 - Binary to Decimal\n2 - Decimal to binary. ")
number = int(input("Number: "))


if op == '1':
	answer = 0
	i = 0
	while  True:
		answer += (number%10)*(2**i)
		number = int(number/10)
		i += 1
		if number == 0:
			break
	print(answer)

else:
	answer = ''
	while True:
		answer += str(number%2)
		number = int(number/2)
		if number / 2 == 0:
			break
	print(answer[::-1])





