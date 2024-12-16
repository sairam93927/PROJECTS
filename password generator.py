import random
import string

def generate_password():
    print("===== Password Generator =====")

    # Prompt the user for the password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be a positive number!")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Display complexity options
    print("\nSelect Password Complexity:")
    print("1. Low (Only lowercase letters)")
    print("2. Medium (Lowercase + Uppercase)")
    print("3. High (Letters + Digits)")
    print("4. Very High (Letters + Digits + Symbols)")

    complexity = input("Enter your choice (1-4): ")

    # Define character sets based on complexity
    if complexity == '1':
        char_set = string.ascii_lowercase
    elif complexity == '2':
        char_set = string.ascii_letters
    elif complexity == '3':
        char_set = string.ascii_letters + string.digits
    elif complexity == '4':
        char_set = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity choice! Please enter a number between 1 and 4.")
        return

    # Generate password
    password = ''.join(random.choice(char_set) for _ in range(length))

    # Display the generated password
    print("\nGenerated Password:")
    print(password)

# Run the password generator
if __name__ == "__main__":
    generate_password()


# second way to genarate a password

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





