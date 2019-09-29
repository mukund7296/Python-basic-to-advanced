
def decofun(fun):
    def inner(n):
        result=fun(n)
        result+="\nHow are you ? "
        return result
    return inner

@decofun
def how(name1):
    return "Hello "+ name1


print(how("Mukund Biradar "))