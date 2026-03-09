
def calculate_gpa(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 90:
        gpa = 10
    elif percentage >= 80:
        gpa = 9
    elif percentage >= 70:
        gpa = 8
    elif percentage >= 60:
        gpa = 7
    elif percentage >= 50:
        gpa = 6
    else:
        gpa = 5

    return percentage, gpa


# main program
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

percentage, gpa = calculate_gpa(marks)

print("\n----- RESULT -----")
print("Student Name:", name)
print("Roll Number:", roll)
print("Marks:", marks)
print("Percentage:", percentage)
print("GPA:", gpa)