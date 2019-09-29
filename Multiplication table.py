# Python Program - Print Multiplication Table of a Number

print("Enter 'x' for exit.");
num = input("Enter a number: ");
print("###############################")
if num == 'x':
    exit();
else:
    number = int(num);
    for i in range(1, 11):
    	print(number, "*", i, "=", number*i);
print("###############################")
for i in range(1,11):
    print(num,"*",i,"=",int(num)*(i))
print("###############################")