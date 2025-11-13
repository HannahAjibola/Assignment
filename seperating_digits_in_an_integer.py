seperate_digits = int(input('Enter five digits integer:'))

first_digit = seperate_digits // 10000

second_digit = seperate_digits // 10 // 10 //10 % 10

third_digit = seperate_digits // 10  // 10 % 10

fourth_digit = seperate_digits // 10 % 10

fifth_digit = seperate_digits % 10

print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit)