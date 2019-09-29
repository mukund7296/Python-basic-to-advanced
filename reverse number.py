
def revers(user):
    if user==user[::-1]:
        return (f"{user} -  Its Reverse")
    else:
      return (f" {user} -its Not reverse ")

user=input("Enter your values :-")
print(revers(user))