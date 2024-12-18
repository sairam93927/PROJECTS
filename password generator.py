import random

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '^', '&', '*']
print("welcome to password genrator")
n_letters=int(input("how many letters you want in your password"))
n_numbers=int(input("how many nubers you want in your password"))
n_symbols=int(input("how many symbols you want in your password"))
password=""
for i in range (1,n_letters):
    char=random.choice(letters)
    password += char
    
for i in range (1,n_numbers):
    char=random.choice(numbers)
    password += char
for i in range (1,n_symbols):
    char=random.choice(symbols)
    password += char
print(password)





