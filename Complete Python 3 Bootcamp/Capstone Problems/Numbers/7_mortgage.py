"""
Mateus H. Ittner - 22/08/18

Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
Also figure out how long it will take the user to pay back the loan. 
For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).


---

A = P * ( (r * (1+r)** n)/ (1+r)** n - 1)

A is the periodic amortization payment
P is the principal amount borrowed
r is the rate of interest expressed as a fraction; for a monthly payment, take the (Annual Rate)/12
n is the number of payments; for monthly payments over 30 years, 12 months x 30 years = 360 payments.


compound formula: 

A = P * (1 + (r/n))**(n*t) 

A is the ending amount, "P" is the beginning amount (or "principal"), "r" is the interest rate (expressed as a decimal), "n" is the number of compoundings a year, and "t" is the total number of years.

Regarding the variables, n refers to the number of compoundings in any one year, not to the total number of compoundings over the life of the investment. 
If interest is compounded yearly, then n = 1; if semi-annually, then n = 2; quarterly, then n = 4; monthly, then n = 12; weekly, then n = 52; daily, then n = 365; and so forth

"""

total = float(input("Enter the borrowed value (in thousands): ")) * 1000
interest = float(input("Enter the yearly interest rate (%): ")) / 100
schedule = input("Compounding interval: Yearly, Monthly, Weekly or Daily? (y,m,w,d)? ")
duration = int(input("Enter the duration (years): "))

if schedule[0].lower() == 'm':
	total = total * (1 + (interest/12))**(12*duration)

elif schedule[0].lower() == "w":
	total = total * (1 + (interest/52))**(52*duration)

elif schedule[0].lower() == "d":
	total = total * (1 + (interest/365))**(365*duration)

else: total = total * (1 + (interest/1))**(1*duration)

monthly = total / 12

print(f"The monthly payment is: ${monthly:.2f}")