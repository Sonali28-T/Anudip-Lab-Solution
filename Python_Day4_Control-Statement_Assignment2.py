#Q2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
#Solution=>>
# Take input from the user
age = int(input("Enter your age: "))

"""Check if the age is 18 or older
If the age is 18 or above, the person is eligible to vote
Otherwise, they are not eligible"""

if age >= 18:
    # If the condition is True, print "You are eligible to vote."
    print("You are eligible to vote.")
else:
    # If the condition is False, print "You are not eligible to vote yet."
    print("You are not eligible to vote yet.")
    
"""ANS=>> Enter your age: 9
          You are not eligible to vote yet.
          Enter your age: 21
          You are eligible to vote."""
