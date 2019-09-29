# Python Program - Calculate Grade of Student

print("Enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
mark1 = input("Enter your Science Numbers :- ");
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input("Enter your English number :-"));
    mark3 = int(input("Enter your Maths Numbers :- "));
    mark4 = int(input("Enter your Chinese Numbers :- "));
    mark5 = int(input("Enter your Social science Numbers :- "));
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=91 and average<=100):
    	print("Your Grade is A+");
    elif(average>=81 and average<=90):
    	print("Your Grade is A");
    elif(average>=71 and average<=80):
    	print("Your Grade is B+");
    elif(average>=61 and average<=70):
    	print("Your Grade is B");
    elif(average>=51 and average<=60):
    	print("Your Grade is C+");
    elif(average>=41 and average<=50):
    	print("Your Grade is C");
    elif(average>=0 and average<=40):
    	print("Your Grade is F");
    else:
    	print("Strange Grade..!!");