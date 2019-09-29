user=int(input("Enter your number :-"))

x=0
while (x<=user):


    x += 1
    if x%10!=0:
        print(x)
        continue
    if x==100:
        break

