# Data streaming is a data technology that allows 
# continuous streams and flows of data from one end to another. 

# Types of Streams:
# Input Stream: Used to read data from a source.
# Output Stream: Used to write data to a destination.

# Python’s Built-in Functions:
# open(): Opens a file stream for reading or writing.
# close(): Closes the opened file.



# Opening a File
# To open a file, you use the open() function. This function takes two arguments:

# 1. The file name or path.
# 2. The mode (like read 'r', write 'w', append 'a', etc.).

# Opening a file in write mode
# file = open('just.txt', 'w')  # 'w' is the mode for writing

# file.write("Hello, World!\n")  # Write data to the file
# file.write("This is a new line of text.\n")
# file.close()  # Close the file manually. VIP


# # with keyword helps to close file automatically
# with open('Section-6 File Handling with Input & Output Features/solid.txt', 'w') as file:  # 'w' mode opens the file for writing
#     file.write("Hello, World!\n")  # Write data to the file
#     file.write("This is a new line of text.\n")
#     file.write("This is a new line of text.\n")
#     file.write("This is a new line of text.\n")
#     file.write("This is a new line of text.\n")


# The with statement ensures that the file is closed properly after 
# the block of code is executed, even if an exception is raised.



# read() Reads the entire file or a specified number of bytes. 
# readline(), or readlines().


with open('solid.txt', 'r') as file:  # 'r' mode opens the file for reading
    content = file.read()  # Reads the entire content of the file
    print(content)



with open('solid.txt', 'r') as file:
    Line1 = file.readline()
    Line2 = file.readline()
    Line3 = file.readline()

    Line4 = file.readline()
    Line5 = file.readline()
    Line6 = file.readline()
    

with open('solid.txt', 'r') as file:
    Line_List = file.readlines()

    print(Line_List)



with open('example.txt', 'r') as f:
    print(f.tell())  # Get current file pointer position
    f.seek(0)  # Move the pointer to the beginning
    print(f.read())  # Read file content from the beginning




# Common Modes:
# 'r': Read (default). The file must exist.
# 'w': Write. Creates a new file or truncates the existing one.
# 'a': Append. Opens a file for appending data.
# 'r+': Read and write. The file must exist.
# 'w+': Write and read. Truncates or creates a new file.



















