# Freelancer Marketplace Simulation

# Lists to store freelancers, clients and projects
freelancers = {}
clients = {}
projects = {}

# Function to register a freelancer
def register_freelancer():
    freelancer_id = input("Enter Freelancer ID: ")
    name = input("Enter Freelancer Name: ")
    skill = input("Enter Freelancer Skill: ")

    freelancers[freelancer_id] = {
        "name": name,
        "skill": skill
    }

    print("Freelancer registered successfully!\n")


# Function to register a client
def register_client():
    client_id = input("Enter Client ID: ")
    name = input("Enter Client Name: ")

    clients[client_id] = {
        "name": name
    }

    print("Client registered successfully!\n")


# Function to assign a project
def assign_project():
    project_id = input("Enter Project ID: ")
    client_id = input("Enter Client ID: ")
    freelancer_id = input("Enter Freelancer ID: ")
    project_name = input("Enter Project Name: ")
    payment = float(input("Enter Project Payment Amount: "))

    if client_id in clients and freelancer_id in freelancers:
        projects[project_id] = {
            "project_name": project_name,
            "client_id": client_id,
            "freelancer_id": freelancer_id,
            "payment": payment,
            "paid": False
        }
        print("Project assigned successfully!\n")
    else:
        print("Invalid Client or Freelancer ID\n")


# Function to process payment
def process_payment():
    project_id = input("Enter Project ID to pay: ")

    if project_id in projects:
        if not projects[project_id]["paid"]:
            projects[project_id]["paid"] = True
            print("Payment processed successfully!")
            print("Amount Paid:", projects[project_id]["payment"], "\n")
        else:
            print("Payment already completed\n")
    else:
        print("Project not found\n")


# Function to display all projects
def show_projects():
    if not projects:
        print("No projects available\n")
        return

    for pid, details in projects.items():
        freelancer_name = freelancers[details["freelancer_id"]]["name"]
        client_name = clients[details["client_id"]]["name"]

        print("\nProject ID:", pid)
        print("Project Name:", details["project_name"])
        print("Client:", client_name)
        print("Freelancer:", freelancer_name)
        print("Payment:", details["payment"])
        print("Paid:", details["paid"])


# Main menu
while True:
    print("\n------ FREELANCER MARKETPLACE ------")
    print("1. Register Freelancer")
    print("2. Register Client")
    print("3. Assign Project")
    print("4. Process Payment")
    print("5. Show Projects")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_freelancer()

    elif choice == "2":
        register_client()

    elif choice == "3":
        assign_project()

    elif choice == "4":
        process_payment()

    elif choice == "5":
        show_projects()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice\n")