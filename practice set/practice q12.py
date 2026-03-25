nums = [5,2,3,2,4,5,1]

unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

for i in range(len(unique)):
    for j in range(i+1,len(unique)):
        if unique[i] > unique[j]:
            unique[i], unique[j] = unique[j], unique[i]

print(unique)