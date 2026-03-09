from datetime import datetime   # To record entry and exit time
import math                     # To round up parking hours

parking = {}        # Dictionary to store vehicle number and entry time
TOTAL_SPOTS = 5     # Total parking capacity
RATE = 20           # Parking fee per hour

while True:         # Infinite loop for menu-driven system
    print("\n1.Entry  2.Exit  3.Available Spots  4.Exit System")
    ch = input("Choose: ")

    # Vehicle Entry
    if ch == "1":
        if len(parking) >= TOTAL_SPOTS:   # Check parking availability
            print("Parking Full")
        else:
            v = input("Vehicle No: ")     # Take vehicle number
            parking[v] = datetime.now()   # Store entry time
            print("Vehicle Entered")

    # Vehicle Exit
    elif ch == "2":
        v = input("Vehicle No: ")
        if v in parking:
            # Calculate parked time in hours
            t = (datetime.now() - parking[v]).total_seconds() / 3600
            fee = math.ceil(t) * RATE     # Round up hours and calculate fee
            del parking[v]                # Remove vehicle from parking
            print("Parking Fee: ₹", fee)
        else:
            print("Vehicle Not Found")

    # Show available parking spots
    elif ch == "3":
        print("Available Spots:", TOTAL_SPOTS - len(parking))

    # Exit the system
    elif ch == "4":
        print("System Closed")
        break

    else:
        print("Invalid Choice")