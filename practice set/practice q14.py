username = input("Enter username: ")
password = input("Enter password: ")

file = open("users.txt","r")
data = file.readlines()

login = False

for line in data:
    u,p = line.strip().split(",")
    
    if u == username and p == password:
        login = True

if login:
    print("Login Successful")
else:
    print("Invalid Login")

file.close()