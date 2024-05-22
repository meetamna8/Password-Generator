import random
import string

def password_generator():
    print("Welcome to the password Generator!")
    max_length = 12

    letters = int(input("How many letters do you want in your password? "))
    digits = int(input("How many digits do you want in your password? "))
    symbols = int(input("How many symbols do you want in your password? "))

    # Check if the total length exceeds the maximum length
    if letters + digits + symbols > max_length:
        print("Total length exceeds the maximum length of 12. Please try again.")
        return password_generator()

    password = []

    for _ in range(letters):
        password.append(random.choice(string.ascii_letters))

    for _ in range(digits):
        password.append(random.choice(string.digits))

    for _ in range(symbols):
        password.append(random.choice(string.punctuation))

    random.shuffle(password)

    return ''.join(password)

print("Generated Password : ", password_generator())