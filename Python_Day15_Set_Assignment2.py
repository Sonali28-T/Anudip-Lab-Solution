#Q2.Write a Python program to Return a set of elements present in Set A or B, but not both.
#Solution=>>

#Define two sets with some numbers
set1 = {10, 20, 30, 40, 50}  
set2 = {30, 40, 50, 60, 70}  

#Use symmetric_difference() to find elements present in either set1 or set2, but not both
result = set1.symmetric_difference(set2)

#Print the result
print("Elements present in either set1 or set2, but not in both:", result)

"""ANS=>>
          Elements present in either set1 or set2, but not in both: {20, 70, 10, 60}

"""
