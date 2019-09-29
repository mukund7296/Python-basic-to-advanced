def pow(x):
    return x**3

print("Power of Number is :-",pow(5))

m=lambda a:a**3
print("Power of Number is :-",m(5))

v=lambda i:i**3
for i in range(1,10):
    print(v(i),end=",")
print("\n#########\n")
odd_even=lambda x:"YES" if x%2==0  else "NO"

print(odd_even(5))
print(odd_even(4))
print(odd_even(3))