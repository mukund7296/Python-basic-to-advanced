print("Enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
m1 = input("Enter your Chinese Number :-");
if m1 == 'x':
    exit();
else:
    m2 = input("Enter Maths Number :-");
    m3 = input("Enter English Number :-");
    m4 = input("Enter Science Numbers:-");
    m5 = input("Enter Hindi Number :-");
    mark1 = int(m1);
    mark2 = int(m2);
    mark3 = int(m3);
    mark4 = int(m4);
    mark5 = int(m5);
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    percentage = (sum/500)*100;
    print("Average Marks = ", average);
    print("Percentage Marks = ", percentage,"%");