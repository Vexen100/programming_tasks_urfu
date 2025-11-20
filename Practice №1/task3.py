import random
import string

# Генерация пароля длины n из символов chars
def generate(chars, n):
    return ''.join([random.choice(chars) for i in range(n)])

password = generate(string.ascii_uppercase, 3) + generate(string.digits, 3) + generate('!@#$%^&*', 2)

print(password)
