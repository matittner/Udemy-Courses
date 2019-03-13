"""
Mateus H. Ittner - 22/08/18
Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

"""

w,h = input("Enter width and height: ").split()
w = float(w) * float(h)
cost = float(input(f"Area of {w:.2f} sqr meters. Enter cost per square meter of tile: "))
print (f"The cost is: ${cost * w:.2f}")
