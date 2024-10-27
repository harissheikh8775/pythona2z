import random

print("Welcome to the PyPassword Generator!")

# Convert inputs to integers
letters_want = int(input("How many letters would you like in your password?\n"))
symbols_want = int(input("How many symbols would you like?\n"))
numbers_want = int(input("How many numbers would you like?\n"))

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']

password = []

# Generate random letters
for _ in range(letters_want):
    password.append(random.choice(letters))

# Generate random symbols
for _ in range(symbols_want):
    password.append(random.choice(symbols))

# Generate random numbers
for _ in range(numbers_want):
    password.append(random.choice(numbers))

# Shuffle the password list to randomize it
random.shuffle(password)

# Join list elements into a single string and print the result
print("Generated Password: ", ''.join(password))
