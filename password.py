import random

posschar = "abcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&*()_+"
ranchar = random.choice(posschar)
print("Want a random password?")
charcount = int(input("How many characters?: "))
if charcount<1:
    print("Please choose an actual amount")
    charcount = int(input("How many characters?: "))
else:
    for i in range(charcount):
        print(ranchar)