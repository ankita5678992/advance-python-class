import re
l=[1,2,2,3,4,4]
r=[]
for i in l:
    if i not in r: r.append(i)
print(r)