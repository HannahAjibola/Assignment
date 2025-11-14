user_password = int(input('input password:'))

if user_password > 6 and user_password <= 10:
	print('medium')

if user_password < 6:
	print('weak')

if user_password > 10:
	print('strong')

if user_password < 1: 
	print('is invalid')