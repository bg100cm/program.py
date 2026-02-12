import random

print("your password;")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
password_length = 12
password = "".join(random.choice(characters) for _ in range(password_length))
print(password)     

