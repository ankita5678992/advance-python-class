file = open("text.txt","r")

data = file.read()

lines = data.split("\n")
words = data.split()
characters = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

file.close()