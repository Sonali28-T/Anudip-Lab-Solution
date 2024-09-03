#Q2.Write a Python program to remove duplicate words of a given string.
#Solution=>>

#Given input string
input_string = "String and String Function"

def remove_duplicate_words(input_string):
    
    #Split the input string into words
    words = input_string.split()
    
    #Initialize an empty list to store unique words
    unique_words = []
    
    #Initialize a set to keep track of words that have been added
    seen = set()
    
    #Loop through each word in the list of words
    for word in words:
        
        #Check if the word has not been seen before
        if word not in seen:
            #Add the word to the list of unique words
            unique_words.append(word)
            #Add the word to the 'seen' set to mark it as encountered
            seen.add(word)
    
    #Join the unique words into a single string with spaces in between
    result = ' '.join(unique_words)

    #Print input string
    print("Given input string is :" , input_string)
    #Print the result
    print("Output string is :", result)

#Call the function with the given input
remove_duplicate_words(input_string)

"""ANS=>> Given input string is : String and String Function
          Output string is : String and Function
"""
