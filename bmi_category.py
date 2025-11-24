weight_kg = float(input("Enter weight:"))
height_meters = float(input("Enter height:"))

bmi = weight_kg / height_meters * height_meters

if bmi <= 18.5:
	print("underweight")

if bmi < 18.5 and bmi <= 24.9:
	print("Normal")

if bmi <= 25 and <= 29.9:
	print("Over weight")

if bmi >= 30:
	print("overweight")