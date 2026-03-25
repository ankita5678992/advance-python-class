import re
a,b=1,20
for n in range(a,b+1):
    if n>1 and all(n%i for i in range(2,n)):
        print(n,end=" ")