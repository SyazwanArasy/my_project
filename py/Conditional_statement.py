# conditional statement

name = str(input("Enter your name: "))
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

# BMI Calculation
bmi = weight / (height**2)

# Input validation
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Output validation
print(f"Hello, {name}!")
print(f"Your BMI is {bmi:.2f}")
print(f"Category: {category}.")