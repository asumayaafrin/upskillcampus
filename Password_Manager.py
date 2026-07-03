import random
import string

passwords = {}

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Strong Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Enter website name: ")
        password = input("Enter password: ")

        passwords[website] = password
        print("Password saved successfully!")

    elif choice == "2":
        website = input("Enter website name: ")

        if website in passwords:
            print("Password:", passwords[website])
        else:
            print("No password found for this website.")

    elif choice == "3":
        length = 10

        characters = string.ascii_letters + string.digits + string.punctuation

        strong_password = ''.join(random.choice(characters) for i in range(length))

        print("Generated Password:", strong_password)

    elif choice == "4":
        website = input("Enter website name to delete: ")

        if website in passwords:
            del passwords[website]
            print("Password deleted successfully!")
        else:
            print("Website not found.")

    elif choice == "5":
        print("Thank you for using Password Manager!")
        break

    else:
        print("Invalid choice! Please try again.")