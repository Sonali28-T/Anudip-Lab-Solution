#Q2. Write a Python program to remove a newline in Python
#Solution=>>

# Define the input string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Print the original string to show how it looks with newlines
print("Original string with newlines:")
print(string)

# Remove newline characters from the string
# Replace '\n' with an empty string ''
cleaned_string = string.replace('\n', '')

# Print the cleaned string without newlines
print("\nIt is string without newlines:")
print(cleaned_string)

"""ANS=>> Original string with newlines:

          Best 
          Deeptech 
          Python 
          Training


          It is string without newlines:
          Best Deeptech Python Training
"""
