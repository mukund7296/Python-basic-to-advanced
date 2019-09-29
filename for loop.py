for i in range(0,10):
    print(" *"*i)
print("################################")

for i in range(0,10):
    for j in range(0,10):
        print(i,j)

print("################################")

i=1
while i<10:
    print(i*" * ")
    i+=1

# Python break Statement Example
print("Welcome to Python break statement.");
count = 0;
while True:
    count += 1;
    if count>10:
        break;
    print(count);