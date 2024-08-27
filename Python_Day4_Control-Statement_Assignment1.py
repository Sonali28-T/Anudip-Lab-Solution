#Q1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
#Solution=>>

# Take input from the user
number = int(input("Enter a number: "))

"""Check if the number is even by using the modulus operator (%)
If the remainder is 0, the number is even; otherwise, it's odd"""
if number % 2 == 0:
    # If the condition is True, print "Even"
    print("Even")
else:
    # If the condition is False, print "Odd"
    print("Odd")
    
"""ANS=>> Enter a number: 12
          Even
          Enter a number: 21
          Odd """

