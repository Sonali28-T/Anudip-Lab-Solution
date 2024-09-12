#Q1.Write a Python program to find the number of times 4 appears in the tuple. 
#Solution=>>

# Define the tuple with a set of integers
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Use the count() method to find how many times the number 4 appears in the tuple
# count() is a built-in tuple method that returns the number of occurrences of a specified value
count_of_4 = tuplex.count(4)

# Print the result showing the count of 4 in the tuple
print("The number 4 appears", count_of_4, "times in the tuple.")

"""ANS=>> The number 4 appears 3 times in the tuple.
"""
