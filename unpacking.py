"""
# Unpacking variables

a, b, c = (1, 2, 3)
print(a, b, c)

a, b, c = [1, 2, 3]

print(a, b, c)
a, b, c = (2 * i + 1 for i in range(3))
print(a, b, c)
a, (b, c), d = [1, (2, 3), 4]
print(a, (b, c), c)

a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)


a = ['Hello', 'world', '!']
for i, x in enumerate(a):
    print ('{}: {}'.format(i, x))


a=10

b="Mukund Biradar"

c=23.40

d=True

print(a)
print(type(a))
print(b)
print(type(b))

print(c)
print(type(c))
print(d)
print(type(d))

cc=[1, (2, 3), 4]



pp=float (3)
print(type(pp))

pp=(3,)
print(type(pp))
dd=tuple(cc)
print(dd)
"""
dict1={1:"INDIA",2:"China",3:"USA"}
dict1.update({4:"Dubai"})
del dict1[3]
print(dict1)

user=[str for x in input("enter your number").split(",")]
print(user)