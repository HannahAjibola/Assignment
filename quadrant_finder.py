first_integer = int(input("Enter first integer:"))
second_integer = int(input("Enter second integer:"))

if first_integer > 0 and second_integer > 0:
	print("Q1")

if first_integer < 0 and second_integer > 0:
	print("Q2")

if first_integer < 0 and second_integer < 0:
	print("Q3")

if first_integer >  0 and second_integer > 0:
	print("Q4")

if first_integer == 0 and second_integer == 0:
	print("Origin")

if second_integer == 0 and first_integer != 0:
	print("X-axis")

if first_integer == 0 and second_integer != 0:
	print("Y-axis")