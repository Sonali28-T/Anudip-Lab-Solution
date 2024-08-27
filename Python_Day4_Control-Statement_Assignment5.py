#Q5.Write a Python program that determines the largest of three numbers entered by the user.
#Solution=>>

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Initialize the variable to store the largest number
# Compare all three numbers using if statements

# Check if num1 is greater than both num2 and num3
if (num1 >= num2) and (num1 >= num3):
    largest = num1
# Check if num2 is greater than num1 and num3
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
# If not num1 or num2, then num3 must be the largest
else:
    largest = num3

# Print the largest number
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")

"""ANS=>> Enter the first number: 34
          Enter the second number: 99
          Enter the third number: 70
          The largest number among 34, 99, and 70 is 99."""
