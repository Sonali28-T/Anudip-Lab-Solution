#Q1. Write a Python program to count the occurrences of each word in a given sentence
#Solution=>>

# Define the input string
string = "To change the overall look of your document. To change the look available in the gallery"
# Remove punctuation (periods and commas) from the string and convert it to lowercase
string = string.replace('.', '').replace(',', '').lower()

# Split the cleaned string into a list of words
words = string.split()

# Create an empty dictionary to store the count of each word
word_count = {}

# Iterate over each word in the list
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_count:
        word_count[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_count[word] = 1

# Print the count of each word
for word, count in word_count.items():
    print(f"'{word}': {count}")
"""ANS=>> 'to': 2
          'change': 2
          'the': 3
          'overall': 1
          'look': 2
          'of': 1
          'your': 1
          'document': 1
          'available': 1
          'in': 1
          'gallery': 1
1"""
