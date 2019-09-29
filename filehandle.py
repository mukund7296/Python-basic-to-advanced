# Python Exceptions - Python Exception Handling - Example Program

try:

    c = open("nosuchfile.txt", 'r')
    print(c.read())
except IOError:
    print("Error in opening the file or the file doesn't exist")
else:
    print("File read successfully..!!")
    c.close()