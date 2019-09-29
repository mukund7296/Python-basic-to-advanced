user=(input("Enter your Number :-"))
total=0
for i in user:
    total=total+int(i)
print(f"Sum of all digits of {user} :-",total)

user=(input("Enter your Number :-"))
total=1
for i in user:
    total=total*int(i)
print(f"multiplication of all digits of {user} :-",total)