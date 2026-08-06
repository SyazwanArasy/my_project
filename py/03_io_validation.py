# Input and Output validation

name = str(input("Enter your name: "))
height = float(input("Enter your height (in cm): "))  # Convert to float

# Input validation
while True:
    try:
        age = int(input("Enter your age: "))  # Convert to integer
        if age > 0 and age < 100:
            break
        else:
            print("Age must be a positive number!")
    except ValueError:
        print("Please enter a valid number!")

# Output validation
print(f"Hello, {name}!")
print(f"Your age is {age} years old and {height} cm tall.")

# Create a simple quiz

#Question 1
while True:
    answer1 = input("What is the capital city of Kelantan? ")
    if answer1 == "Kota Bharu" or answer1 == "kota bharu":
        print("Correct!")
        break
    else:
        print("Incorrect.")
        break

#Question 2
while True:
    answer2 = input("What is 5 + 7? ")
    if answer2 == "12":
        print("Correct!")
        break
    else:
        print("Incorrect.")
        break
        

#Question 3
while True:
    answer3 = input("What is the largest planet in our solar system? ")
    if answer3 == "jupiter" or answer3 == "Jupiter":
        print("Correct!")
        break
    else:
        print("Incorrect.")
        break

#Score calculation
score = 0
if answer1 == "kota bharu" or answer1 == "Kota Bharu":
    score += 1
else:
    score += 0
if answer2 == "12":
    score += 1
else:
    score += 0
if answer3 == "jupiter" or answer3 == "Jupiter":
    score += 1
else:
    score += 0

# Output the score
if score == 3:
    print("Your score is 3/3. Excellent!")
elif score == 2:
    print("Your score is 2/3. Good job!")
else:
    print("You got less than 2 correct. Better luck next time!")