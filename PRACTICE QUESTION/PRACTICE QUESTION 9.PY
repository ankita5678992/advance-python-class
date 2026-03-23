emp = {}

while True:
    print("1.Add 2.Remove 3.Display 4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Enter name: ")
        emp[name] = "Present"

    elif ch == 2:
        name = input("Remove name: ")
        emp.pop(name, None)

    elif ch == 3:
        print(emp)

    else:
        break