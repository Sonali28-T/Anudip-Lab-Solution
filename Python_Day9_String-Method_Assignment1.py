#Q1.Write a Python program to Count all letters, digits, and special symbols from the given string
#Solution=>>

#Given input string
input_string = "P@#yn26at^&i5ve"
def count_chars_digits_symbols(input_string):
    #Initialize counters
    letter_count = 0
    digit_count = 0
    symbol_count = 0
    
    #Loop through each character in the string
    for char in input_string:  #Increment the letter count
        #Check if the character is a letter
        if char.isalpha():
            letter_count += 1    #Increment the digit count
        #Check if the character is a digit
        elif char.isdigit():
            digit_count += 1
        #If it is neither a letter nor a digit, it is a symbol
        else:
            symbol_count += 1  #Increment the symbol count
    
    #Print the total count of letters, digits and symbols
    print("Given String is : P@#yn26at^&i5ve")
    print("Chars in given string:", letter_count)
    print("Digits in given string:", digit_count)
    print("Symbols in given string:", symbol_count)


#Call the function with the example input to count characters, digits, and symbols
count_chars_digits_symbols(input_string)


"""ANS=>>  Given String is : P@#yn26at^&i5ve
           Chars in given string: 8
           Digits in given string: 3
           Symbols in given string: 4"""
