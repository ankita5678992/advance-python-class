contacts = {}

while True:
    print("1.Add 2.Search 3.Delete 4.Show 5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == 2:
        name = input("Search: ")
        print(contacts.get(name, "Not found"))

    elif ch == 3:
        name = input("Delete: ")
        contacts.pop(name, None)

    elif ch == 4:
        print(contacts)

    else:
        break