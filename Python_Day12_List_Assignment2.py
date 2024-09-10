#Q2. Write a Python program to get the largest and smallest number from a list without builtin functions. 
#Solution=>>

#Function to find the largest and smallest numbers in a list
def find_largest_smallest(numbers):
    #Initialize the largest and smallest variables with the first element of the list
    #This sets a baseline for comparison with the rest of the list elements
    largest = numbers[0]
    smallest = numbers[0]

    #Loop through the rest of the list starting from the second element
    for num in numbers[1:]:
        #If the current number is greater than the current largest, update largest
        if num > largest:
            largest = num  #Update the largest number to the current number

        #If the current number is smaller than the current smallest, update smallest
        if num < smallest:
            smallest = num  #Update the smallest number to the current number

    #Return both the largest and smallest numbers after checking all elements
    return largest, smallest

#List of numbers
numbers = [10, 28 , 45, 99, 67, 7, 50]

#Call the function to find the largest and smallest numbers in the list
largest, smallest = find_largest_smallest(numbers)

#Print the largest number in the list with a meaningful message
print("The largest number in the list is:", largest)

#Print the smallest number in the list with a meaningful message
print("The smallest number in the list is:", smallest)

"""ANS=>>
         The largest number in the list is: 99
         The smallest number in the list is: 7
"""
