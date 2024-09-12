#Q2.Write a Python script to concatenate the following dictionaries to create a new one. 
#Solution=>>

#Define the three sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

#Create a new empty dictionary to store the concatenated result
result_dict = {}

#Use the update() method to add key-value pairs from each dictionary to result_dict
result_dict.update(dic1)  # Add all key-value pairs from dic1
result_dict.update(dic2)  # Add all key-value pairs from dic2
result_dict.update(dic3)  # Add all key-value pairs from dic3

#Print the resulting concatenated dictionary
print("Concatenated dictionary:", result_dict)

"""ANS=>>
         Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""
