menu = {"Pizza": 100, "Burger": 50, "Tea": 20}
total = 0

while True:
    print(menu)
    item = input("Enter item (or exit): ")

    if item == "exit":
        break

    if item in menu:
        qty = int(input("Quantity: "))
        total += menu[item] * qty

tax = total * 0.05
print("Total:", total)
print("Tax:", tax)
print("Final Bill:", total + tax)