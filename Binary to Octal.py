# Python Program - Convert Binary to Octal

print("Enter 'x' for exit.")
binary = input("Enter any number in Binary Format: ")
if binary == 'x':
    exit()
else:
    temp = int(binary, 2)
    print(binary,"in Octal =",oct(temp))