#Q3.Write a Python program to find duplicate values from a list and display those
#Solution=>>

#Function to find and display duplicate values from a list
def find_duplicates(numbers):
    #Initialize an empty list to store numbers that are duplicates
    duplicates = []

    #Iterate through each number in the list
    for num in numbers:
        #Check if the number appears more than once in the list
        #and if it has not already been recorded as a duplicate
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)  # Add the number to the duplicates list

    #Return the list of duplicate numbers
    return duplicates

#List with some numbers containing duplicates
numbers = [7, 7, 8, 12, 16, 23, 42, 12, 9, 23, 42, 99 , 28 ,99, 23, 9]
print("The original list is:", numbers)

#Call the function to find duplicate values in the list
duplicates = find_duplicates(numbers)

#Check if any duplicates were found
if duplicates:
    #Print the duplicate values found in the list
    print("The duplicate values in the list are:", duplicates)
else:
    #Print a message if no duplicates were found in the list
    print("No duplicate values found in the list.")

"""Ans=>>
          The original list is: [7, 7, 8, 12, 16, 23, 42, 12, 9, 23, 42, 99, 28, 99, 23, 9]
          
          The duplicate values in the list are: [7, 12, 23, 42, 9, 99]
"""

