# Python Program - Display Calendar

import calendar
print("------Calendar Program in Python------\n")
print("Enter 'x' for exit.")
y = input("Enter Year: ")
if y == 'x':
    exit()
else:
    m = input("Enter month: ")
    yy = int(y)
    mm = int(m)
    print("\n",calendar.month(yy,mm))