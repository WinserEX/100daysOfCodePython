#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Length of arrays
l = len(letters)
s = len(symbols)
n = len(numbers)

password = []
#Letters
for i in range(0,nr_letters):
    randL = random.randint(0,l -1) 
    for x in letters[randL]:
        password.append(x)
        print(f'{i} Letters')
#Symbols
for i in range(0,nr_symbols):
    randS = random.randint(0,s -1) 
    for x in symbols[randS]:
        password.append(x)
        print(f'{i} Symbols')
#Numbers
for i in range(0,nr_numbers):
    randN = random.randint(0,n -1)
    for x in numbers[randN]:
        password.append(x)
        print(f'{i} Numbers')

p = len(password)
passStr = ' '

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for i in range(0,p):
    randPass = random.randint(0,p -1)
    for x in password[randPass]:
        passStr += x

print(f"Your password is {passStr}")

