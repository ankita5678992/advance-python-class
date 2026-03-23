students = {"Aman": 80, "Riya": 90}

students["John"] = 75      # Add
students["Aman"] = 85      # Update
del students["Riya"]       # Delete

print("Keys:", students.keys())
print("Values:", students.values())
print("Items:", students.items())