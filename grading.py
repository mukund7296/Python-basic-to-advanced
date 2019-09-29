
#grading system
Ma = int(input("Enter your Maths :- "))
if Ma<=35:
    print("Your are Failed. ")
    exit()
Py = int(input("Enter your Physics :- "))
if Py<=35:
    print("Your are Failed. ")
    exit()
Ch = int(input("Enter your Chemsitry  :- "))
if Ch<=35:
    print("Your are Failed. ")
    exit()
avg=(Ma+Py+Ch)/3

print("Total Marks are ",avg,"out of 300")
if avg<=59:
    print("Grade C")
elif avg<69:
    print("Grade B")
elif avg>=69:
    print("Grade A")