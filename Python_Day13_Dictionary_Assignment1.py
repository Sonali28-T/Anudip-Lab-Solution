#Q1.Write a Python program and calculate the mean of the below dictionary.
#Solution=>>

#Define the dictionary with key-value pairs
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

#Calculate the total sum of the values in the dictionary
#sum() function adds up all the values (6 + 9 + 5 + 7 + 4 = 31)
total_sum = sum(test_dict.values())

#Calculate the number of elements (key-value pairs) in the dictionary
#len() function returns the count of items (in this case, 5 items)
num_elements = len(test_dict)

#Calculate the mean (average) by dividing the total sum by the number of elements
#Formula for mean: mean = total_sum / num_elements (31 / 5 = 6.2)
mean = total_sum / num_elements

# The output will show the average value of all the dictionary values
print("The mean of the dictionary values is:", mean)

"""ANS=>>
          The mean of the dictionary values is: 6.2
"""
