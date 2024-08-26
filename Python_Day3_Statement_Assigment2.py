# Q2. Using input function take two number and then swap the number
# Solution=>>

# Take two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display the values before swapping
print(f"Before swapping: First number is : {num1}, Second number is : {num2}")

# Swap the numbers
num1, num2 = num2, num1

# Display the values After swapping
print(f"After swapping: First number is : {num1}, Second number is : {num2}")

"""ANS=>> Enter the first number: 7
          Enter the second number: 9
          Before swapping: First number is : 7, Second number is : 9
          After swapping: First number is : 9, Second number is : 7"""


