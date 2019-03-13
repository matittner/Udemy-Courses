"""
Mateus H. Ittner - 22/08/18

Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. 
The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

----

Unfinished (it would be the same for every type of conversion)

"""

def currency():

	print("(D) Dollar")
	print("(E) Euro")
	print("(R) Real")
	print("(Y) Yen")

	first = input("From: ").lower() # gets the dict key 
	amount = float(input("Amount: "))
	second = input("To: ").lower()
	
	d={'e': 0.86, 'r': 4.08,'y':110.36,'X':'$'}
	e={'d': 1.16, 'r': 4.72,'y':128.06,'X':'€'}
	r={'d': 0.25, 'e': 0.21,'y':27.12,'X':'R$'}
	y={'d': 0.0091, 'e': 0.0078,'r':0.037,'X':'¥'}

	options = {'d':d,'e':e,'r':r,'y':y}


	print(f"Result = {options[second]['X']}{options[first][second] * amount:.2f}") # matches dict keys to get the right conversion ratio


def energy():

	print("(B) Btu")
	print("(C) Calories")
	print("(J) Joules")
	print("(L) Gasoline")

	first = input("From: ").lower()
	amount = float(input("Amount: "))
	second = input("To: ").lower()
	
	b={'c': 0.251875, 'j': 1054.35,'l':0.000031,'X':'Btu'}
	c={'b': 3.970219, 'j': 4186,'l':0.000122,'X':'calories'}
	j={'b': 0.000948, 'c': 0.000239,'l':7.5895567698846e-9,'X':'joules'}
	l={'b': 32437.046522, 'c': 8170.090779,'j':34200000,'X':'liters of gasoline'}

	options = {'b':b,'c':c,'j':j,'l':l}


	print(f"Result = {options[first][second] * amount} {options[second]['X']}") 



def lenght():
	pass

def mass():
	pass

def power():
	pass

def speed():
	pass

def temperature():
	pass

def time():
	pass	

def volume():
	pass

print("(C) Currency")
print("(E) Energy")
print("(L) Lenght")
print("(M) Mass")
print("(P) Power")
print("(S) Speed")
print("(T) Temperature")
print("(I) Time")
print("(V) Volume")

user = input().lower()

options = {'c':currency,'e':energy, 'l':lenght, 'm':mass,'p':power,'s':speed,'t':temperature,'i':time,'v':volume}

options[user]() # uses a dict to call the right function 






