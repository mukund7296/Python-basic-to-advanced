# Python Program - One Dimensional Array

print("Enter 'x' for exit.")
nval = input("How many element you want to store in the array ? ")
if nval == 'x':
    exit()
else:
    n = int(nval)
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    print("\nElements in Array are:")
    for i in range(0, n):
        print(arr[i], end=" ")