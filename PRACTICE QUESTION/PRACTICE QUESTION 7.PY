students = {}

def add_student(name, marks):
    students[name] = marks

def update_marks(name, marks):
    students[name] = marks

def average(name):
    return sum(students[name]) / len(students[name])

def topper():
    return max(students, key=lambda x: sum(students[x]))

add_student("Aman", [80, 90])
add_student("Riya", [85, 95])

print("Average Aman:", average("Aman"))
print("Topper:", topper())