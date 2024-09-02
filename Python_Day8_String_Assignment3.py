#Q3. Write a Python program to reverse words in a string 
#Solution=>>
# Define the input string
string = "Deeptech Python Training"

# Print the original string
print("Original string:")
print(string)

# Split the string into a list of words
words = string.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed list back into a single string with spaces
reversed_string = ' '.join(reversed_words)

# Print the reversed string
print("\nString with words reversed:")
print(reversed_string)

"""ANS=>> Original string:
          Deeptech Python Training

          String with words reversed:
          Training Python Deeptech
"""
