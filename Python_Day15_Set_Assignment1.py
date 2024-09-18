#Q1. Write a Python program to Get Only unique items from two sets. 
#Solution=>>

#Define two sets with some numbers
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70}  

#Use union() to combine both sets and remove duplicates
unique_items = set1.union(set2)  # This will combine the sets and keep only unique items

#Print the unique items from both sets
print("Unique items from both sets:", unique_items)  


"""ANS=>>
         Unique items from both sets: {70, 40, 10, 50, 20, 60, 30}
"""
