first_integer = int(input("Enter first integer:"))
second_integer = int(input("Enter second integer:"))

if second_integer != 0:
	sum = first_integer / second_integer
	print(sum)
	
else:
	print("cannot divide by zero")