#2.Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number.
#Solution=>>

# Define a function named 'square' that takes one parameter 'n'
def square(n):
    
    # Return the square of 'n' using the pow() function
    # The pow() function is a built-in Python function that raises the first argument 'n' to the power of the second argument, which is 2 in this case

    return pow(n, 2)

# Call the 'square' function with a number as an argument
result = square(6)

# Display the square of the number in the desired format
print(f"The square of 6 is {result}.")

#ANS=> The square of 6 is 36.


