password = input("Please enter the password:")

while len(password) <= 0:
    print("Invalid password.")
    password = input("Please enter the password.")
encrypt_password = '*' * len(password)
print(encrypt_password)