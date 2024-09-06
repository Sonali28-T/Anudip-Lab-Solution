#1.Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
#Solution=>>

def read_file():
    #Open the file "ABC.txt" in read mode
    file = open("ABC.txt", "r")
    
    #Loop through each line in the file
    for line in file:

        #Print the current line after removing any extra spaces or newlines
        print(line.strip())
    
    #Close the file after reading
    file.close()

#Example usage of the function to read and display the file contents
read_file()


"""ANS=>>
Hello I'm Sonali today I learn File I/O

In Python, File I/O (Input/Output) refers to reading from or writing to a file on your system.

"""
