#4. Python program to find the area of a triangle whose sides are given

# Lengths of the sides of the triangle
side1 = 3
side2 = 5
side3 = 7
# Calculate the semi-perimeter
s = (side1 + side2 + side3) / 2  #s is computed as half of the sum of the sides.

# Calculate the area using Heron's formula
#The ** operator in Python is used for raising a number to a power, and ** 0.5 calculates the square root of a number by raising it to the power of 0.5.
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5 

# Print the result
print("Area of the triangle:", area)


#ANS=>> Area of the triangle: 6.49519052838329
