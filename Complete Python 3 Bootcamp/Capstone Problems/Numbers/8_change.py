"""
Mateus H. Ittner - 22/08/18

Change Return Program - The user enters a cost and then the amount of money given. 
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

---

https://docs.python.org/2/tutorial/floatingpoint.html

"""

cost = float(input("Cost: $"))
given = float(input("Given: $"))
change = given - cost
change = round(change,2)
print(f"Your change is ${change}") 
if change != 0:
	print("You will receive: ")  # go removing coins until change == 0
	if change > 0.25:
		coin = int(change/ 0.25)
		print(f"{coin} quarters")
		change = float(change - coin * 0.25)
		change = round(change,2)
	if change != 0 and change >= 0.1:
		coin = int(change/ 0.1)
		print(f"{coin} dimes")
		change = float(change - coin * 0.1)
		change = round(change,2)
	if change != 0 and change >= 0.05:
		coin = int(change/ 0.05)
		print(f"{coin} nickels")
		change = float(change - coin * 0.05)
		change = round(change,2)
	if change != 0 and change >= 0.01:
		coin = int(change/ 0.01)
		print(f"{coin} pennies")
		change = float(change - coin * 0.01)



