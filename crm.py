# Customer Relationship Manager (CRM) System
# This program stores customer information and communication logs

# Dictionary to store customer details
customers = {}

# Function to add a new customer
def add_customer():
    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")

    customers[customer_id] = {
        "name": name,
        "email": email,
        "phone": phone,
        "logs": []   # list to store communication logs
    }

    print("Customer added successfully!\n")


# Function to add communication log
def add_log():
    customer_id = input("Enter Customer ID: ")

    if customer_id in customers:
        message = input("Enter communication message: ")
        customers[customer_id]["logs"].append(message)
        print("Log added successfully!\n")
    else:
        print("Customer not found!\n")


# Function to view customer details
def view_customer():
    customer_id = input("Enter Customer ID: ")

    if customer_id in customers:
        customer = customers[customer_id]

        print("\nCustomer Details")
        print("Name:", customer["name"])
        print("Email:", customer["email"])
        print("Phone:", customer["phone"])

        print("Communication Logs:")
        for log in customer["logs"]:
            print("-", log)

        print()
    else:
        print("Customer not found!\n")


# Function to show all customers
def show_all_customers():
    if not customers:
        print("No customers available.\n")
    else:
        for cid, info in customers.items():
            print(f"ID: {cid}, Name: {info['name']}, Email: {info['email']}, Phone: {info['phone']}")
        print()


# Main menu
while True:
    print("Customer Relationship Manager")
    print("1. Add Customer")
    print("2. Add Communication Log")
    print("3. View Customer")
    print("4. Show All Customers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        add_log()
    elif choice == "3":
        view_customer()
    elif choice == "4":
        show_all_customers()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")