# Import required libraries
import base64
import json
import os

# File to store passwords
FILE_NAME = "password_store.json"


# Function to encrypt password
def encrypt_password(password):
    # convert password to bytes then encode using base64
    encoded = base64.b64encode(password.encode())
    return encoded.decode()


# Function to decrypt password
def decrypt_password(encoded_password):
    # decode base64 back to original password
    decoded = base64.b64decode(encoded_password.encode())
    return decoded.decode()


# Function to load stored passwords
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# Function to save passwords
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)


# Add new password
def add_password(data):
    site = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    encrypted = encrypt_password(password)

    data[site] = {
        "username": username,
        "password": encrypted
    }

    save_data(data)
    print("Password saved successfully!")


# View password
def view_password(data):
    site = input("Enter website name: ")

    if site in data:
        decrypted = decrypt_password(data[site]["password"])
        print("Username:", data[site]["username"])
        print("Password:", decrypted)
    else:
        print("No record found.")


# Edit password
def edit_password(data):
    site = input("Enter website name to edit: ")

    if site in data:
        new_password = input("Enter new password: ")
        data[site]["password"] = encrypt_password(new_password)
        save_data(data)
        print("Password updated.")
    else:
        print("Site not found.")


# Delete password
def delete_password(data):
    site = input("Enter website name to delete: ")

    if site in data:
        del data[site]
        save_data(data)
        print("Password deleted.")
    else:
        print("Site not found.")


# Main program
def main():
    data = load_data()

    while True:
        print("\nPASSWORD MANAGER")
        print("1. Add Password")
        print("2. View Password")
        print("3. Edit Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password(data)

        elif choice == "2":
            view_password(data)

        elif choice == "3":
            edit_password(data)

        elif choice == "4":
            delete_password(data)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


# Run program
main()