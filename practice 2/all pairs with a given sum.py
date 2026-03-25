import re
l=[1,2,3,4,5]
s=6
for i in l:
    for j in l:
        if i+j==s and i<j: print(i,j)