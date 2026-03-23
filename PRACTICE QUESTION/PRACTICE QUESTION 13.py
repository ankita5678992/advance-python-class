s = input("Enter sentence: ")

result = []
for ch in s:
    if ch.isalnum() and s.count(ch) == 1:
        result.append(ch)

print("Unique characters:", result)