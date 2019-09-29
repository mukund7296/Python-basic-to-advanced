"""print("Enter 'x' for exit.");
print("Enter any five numbers: ");
num1 = input();
if num1 == 'x':
    exit();
else:
    num2 = input();
    num3 = input();
    num4 = input();
    num5 = input();
    number1 = int(num1);
    number2 = int(num2);
    number3 = int(num3);
    number4 = int(num4);
    number5 = int(num5);
    numbers_list = [number1, number2, number3, number4, number5,];
    check_num = int(input("Enter a number to check divisibility test: "));
    res = list(filter(lambda x: (x % check_num == 0), numbers_list));
    print("Number divisible by",check_num,"are",res);
   """
num1=  int(input("Enter your number :- "))
num2 = int(input("Enter your number :- "))
num3 = int(input("Enter your number :- "))
num4 = int(input("Enter your number :- "))
num5 = int(input("Enter your number :- "))

store=[num1,num2,num3,num4,num5]
check_num = int(input("Enter a number to check divisibility test: "));
for i in store:
    if i%check_num==0:
        print(i,end="  ")

#print(store)
