# find the Find Factorial of Number

def facto(x):
    if x==0:
        return 1
    else:
        return x*facto(x-1)

num1=int(input("Enter Your Number :- "))
print(f"Factorial of", {num1}, "is :- ",facto(num1))