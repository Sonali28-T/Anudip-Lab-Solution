# Q1.Using input() function take one number from the user and using ternary operators check whether the number is even or odd 
# Solution:=>

# Taking input from the user
number = int(input("Enter a number: "))

# Checking if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

""" Displaying the result: The f-string formats the string by replacing {number} and {result} with their respective values.
                           The print() function displays the output to the screen."""

print(f"The number {number} is {result}.")

"""ANS=>> Enter a number: 7
      =>> The number 7 is Odd.
            OR
   ANS=>> Enter a number: 6
      =>> The number 6 is Even."""
