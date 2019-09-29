user=int(input("Enter your Number :-"))
total=0
for i in range(0,user+1):
    total=total+int(i)
print(f"Sum of all digits of {user} :-",total)