num1=  int(input("Enter your number :- "))
total=[]
for i in range(0,num1+1):
    total.append(i)
print(total)
print((total[::-1]))
num2= (input("Enter your number :- "))
def rever(x):
    return x[::-1]

print(rever(num2))