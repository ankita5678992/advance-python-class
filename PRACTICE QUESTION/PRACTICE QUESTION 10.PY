students = []

while True:
    print("1.Add 2.Show Pass 3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Name: ")
        roll = int(input("Roll: "))
        marks = int(input("Marks: "))
        students.append({"name": name, "roll": roll, "marks": marks})

    elif ch == 2:
        for s in students:
            if s["marks"] >= 40:
                print(s)

    else:
        break