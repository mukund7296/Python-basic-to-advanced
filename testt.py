class A:
    @staticmethod
    def a(x):
        print(x)
A.a(100)


def ordi():
    print("Ordinary")


ordi
ordi()

print (r"\nhello")

print()



for i in range(5):
    if i == 5:
        break
    else:
        print(i)
else:
    print("Here")

x = 'abcd'
for i in range(len(x)):
    print(x)
    x = 'a'


print(max("what are you"))

string = "my name is x"
for i in string.split():
    print (i, end=", ")