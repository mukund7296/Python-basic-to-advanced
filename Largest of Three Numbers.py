# find the Largest of Three Numbers
num1=int(input("Enter Your First Number :- "))
num2=int(input("Enter Your 2nd Number :- "))
num3=int(input("Enter Your 3rd Number :- "))

if num1>num2 and num1>num3:
    print(f" {num1} is largest Number ")
elif num2>num1 and num2>num3:
    print(f" {num2} is largest Number ")
elif num3>num1 and num3>num2:
    print(f" {num3} is largest Number ")