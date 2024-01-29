import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

print("Want a random password?")
countlower = int(input("How many lowercase characters?: "))
countupper = int(input("How many uppercase characters?: "))
countnum = int(input("How many numeral characters?: "))
countsymb = int(input("How many special characters?: "))

while countlower < 1 or countupper < 1 or countnum < 1 or countsymb < 1:
    print("Please choose an actual amount")
    countlower = int(input("How many lowercase characters?: "))
    countupper = int(input("How many uppercase characters?: "))
    countnum = int(input("How many numeral characters?: "))
    countsymb = int(input("How many special characters?: "))

password = ""
for i in range(countlower):
    password += random.choice(ascii_lowercase)
for i in range(countupper):
    password += random.choice(ascii_uppercase)
for i in range(countnum):
    password += random.choice(digits)
for i in range(countsymb):
    password += random.choice(punctuation)

print(''.join(random.sample(password, len(password))))