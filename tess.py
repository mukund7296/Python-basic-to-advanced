m, p, c = [int(x) for x in input("Enter final grades for the subjects: ").split()]
if m < 35 or p < 35 or c < 35:
    print("The student has failed the exams")
else:
    grade = (m + p + c) / 3
    if grade <= 59:
        print("Your grade was C")
    elif grade > 59 and grade <= 69:
        print("Your grade was B")
    else:
        print("Your grade was A")