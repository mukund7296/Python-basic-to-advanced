i = 5
while True:
    if i%0O11 == 0:
        break
    print(i)
    i += 1
def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
def mk2():
    print("Ordinary")
p = mk(mk2)
p()

print(format("Welcome", "10s"), end = '#')
print(format(111, "4d"), end = '#')
print(format(924.656, "3.2f"))

for i in '':
    print (i)