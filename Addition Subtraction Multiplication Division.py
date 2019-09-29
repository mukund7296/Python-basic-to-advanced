num1=int(input("Enter your first Number :-  "))
num2=int(input("Enter your second Number.:- "))
option=int(input("0.Exit.\n1. Addition:\n2. Subtraction:\n3. Multiplication:\n4. Division:\nOption Here :"))
if option==0:
    print(f" Exit ")
if option==1:
    print(f" Addition of {num1} And {num2} is :- {num1+num2}")
elif option==2:
    print(f" Subtraction of {num1} And {num2} is :- {num1-num2}")
elif option==3:
    print(f" Multiplication of {num1} And {num2} is :- {num1*num2}")
elif option==4:
    print(f" Division of {num1} And {num2} is :- {num1/num2}")
