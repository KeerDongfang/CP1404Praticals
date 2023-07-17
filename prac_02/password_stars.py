def main():
    password = input("Please enter the password:")
    check_password_validity(password)


def check_password_validity(password):
    """check whether the password is valid and print the result"""
    while len(password) <= 0:
        print("Invalid password.")
        password = input("Please enter the password.")
    encrypt_password = '*' * len(password)
    print(encrypt_password)


main()
