#Q4.Create a Python program that checks if a user-given number is positive, negative, or zero.
#Solution=>>

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
# Use conditional statements to determine the type of number

if number > 0:
    # If the number is greater than 0, it is positive
    print(f"The number {number} is positive.")
elif number < 0:
    # If the number is less than 0, it is negative
    print(f"The number {number} is negative.")
else:
    # If the number is neither greater than 0 nor less than 0, it must be zero
    print("The number is zero.")
"""ANS=>> Enter a number: 7
          The number 7 is positive.
          Enter a number: -3
          The number -3 is negative.
          Enter a number: 0
          The number is zero."""
