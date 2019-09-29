
def armstr(x):
    total=0
    for i in x:
        total=total+(int(i)**3)

    if int(x)==total:
        return ("Is an Armstrong Number.")
    else:
        return ("Not Armstrong Number.")



user=(input("Enter your number :- "))

print(armstr(user))