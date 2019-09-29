"""
f(n)=0   0
f(n)=1   1
f(n)=f(n-1)+f(n-2)

"""

def fibo(x):
    if x<=0:
        return x
    elif x==1:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)

user=int(input("Enter your Number :-"))

for i in range(1,user+1):
    print(fibo(i))