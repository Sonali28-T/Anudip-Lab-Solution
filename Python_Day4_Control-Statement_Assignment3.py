#Q3.Write a Python program that determines if a given year is a leap year or not.
#Solution=>>

# Take input from the user
year = int(input("Enter a year: "))

""" Determine if the year is a leap year
    A year is a leap year if:
    1. It is divisible by 4
    2. It is not divisible by 100, unless it is also divisible by 400"""

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    
    # If the year satisfies the conditions for a leap year, print "The year is a Leap year"
    print(f"The year {year} is a Leap year.")
else:
    # If the year does not satisfy the leap year conditions, print "The year is Not a leap year"
    print(f"The year {year} is Not a Leap year.")

"""ANS=>> Enter a year: 2022
          The year 2022 is Not a Leap year.
          Enter a year: 2020
          The year 2020 is a Leap year."""


