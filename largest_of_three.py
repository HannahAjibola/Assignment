first_int = int(input("Enter first number:"))
second_int = int(input("Enter second number:"))
third_int = int(input("Enter third number:"))

largest = first_int 

if second_int > largest:
	largest = second_int

if third_int > largest:
	largest = third_int
print("The largest number is", largest)

