def main():
    """main function"""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        user_name = extract_name(email)
        name_validation = input(f"Is your name {user_name}? (Y/N) ")
        if name_validation.upper() != "Y" and name_validation != "":
            user_name = input("Name: ")
        email_to_name[email] = user_name
        email = input("Email: ")

    print("\nEmails and Names:")
    for email, user_name in email_to_name.items():
        print(f"{user_name} ({email})")


def extract_name(email):
    """extract user name from email address"""
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name


main()
