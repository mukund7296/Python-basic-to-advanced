num = int(input("Enter you number "))

if num > 1:
    for i in range(2, num-1):
        if (num % i)  == 0:
            print(num, "is no Primenumber")
            break
        else:
            print(i, "PRIME!!!")