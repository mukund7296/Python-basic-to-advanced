# Python Program - Pattern Program 1

for i in range(0, 5):
    for j in range(0, i + 1):
        print("* ", end="")
    print()


# Python Program - Pattern Program 2

k = 1
for i in range(0, 5):
    for j in range(0, k):
        print("* ", end="")
    k = k + 2
    print()

# Python Program - Pattern Program 6

for i in range(0, 5):
    num = 1
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1
    print()