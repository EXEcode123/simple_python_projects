import random
import string

def generate_password(length=12, include_symbols=True):
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password = generate_password()
print(f'Generated Password: {password}')
