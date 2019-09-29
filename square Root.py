# Python Program - Find Square Root of a Number

print("Enter 'x' for exit.");
num = input("Enter a number: ");
if num == 'x':
    exit();
else:
    number = float(num);
    number_sqrt = number ** 0.5;
    print("Square Root of %0.2f is %0.2f" %(number, number_sqrt));
print("###################################")
num1=float(num)**0.5
print(f"Square Root of {float(num)} is :" ,num1)