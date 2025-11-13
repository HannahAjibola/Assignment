first_integer = int(input('Enter first integer:'))

second_integer = int(input('Enter second integer:'))

third_integer = int(input('Enter third integer:'))

total_sum = first_integer + second_integer + third_integer

print('sum is', total_sum)

total_average = total_sum // 2

print('average is:', total_average)

total_product = first_integer * second_integer * third_integer

print('product is:', total_product)

small = first_integer

if second_integer < small:
	small = second_integer 

if third_integer < small:
	small = third_integer

print('The smallest number is:', small)

large = first_integer

if second_integer > large:
	large = second_integer

if third_integer > large:
	large = third_integer

print('The largest number is:', large)


